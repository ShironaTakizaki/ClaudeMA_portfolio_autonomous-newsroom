"""
Entry point for the autonomous publishing pipeline.

Usage:
  python src/main.py publish   # daily article generation
  python src/main.py reap      # delete expired articles
  python src/main.py zen       # ZEN cycle (thinker distillation)
"""
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import anthropic

from zen_search import load_recently_used_zen

AGENTS_PATH = Path(__file__).parent.parent / "agents"
ARTICLES_PATH = Path(__file__).parent.parent / "articles"
KNOWLEDGE_PATH = Path(__file__).parent.parent / "knowledge"
ASSETS_PATH = Path(__file__).parent.parent / "assets"

client = anthropic.Anthropic()


def load_system(name: str) -> str:
    return (AGENTS_PATH / f"{name}.md").read_text()


def call(system: str, user: str, model: str = "claude-opus-4-7", tools: list | None = None) -> str:
    """Call the Messages API and return the final text response.

    web_search_20250305 is a server-side tool: the API executes it automatically.
    pause_turn means the API paused mid-server-tool; append and continue.
    Client never needs to send tool_result for server-side tools.
    """
    messages: list[dict] = [{"role": "user", "content": user}]
    kwargs: dict = dict(model=model, max_tokens=4096, system=system)
    if tools:
        kwargs["tools"] = tools

    while True:
        response = client.messages.create(**kwargs, messages=messages)
        if response.stop_reason == "end_turn":
            return "".join(b.text for b in response.content if hasattr(b, "text"))
        if response.stop_reason == "pause_turn":
            messages.append({"role": "assistant", "content": response.content})
            continue
        # tool_use (client-side) or unexpected — return what we have
        return "".join(b.text for b in response.content if hasattr(b, "text"))


def slug(title: str, published: str) -> str:
    date_str = published[:10]
    safe = re.sub(r"[^\w\s-]", "", title.lower())[:40].strip().replace(" ", "-")
    return f"{date_str}-{safe}"


# ── Pipeline steps ────────────────────────────────────────────────────────────

def step_curator(today: str) -> dict:
    """Select today's news item."""
    result = call(
        system=load_system("curator"),
        user=f"Today is {today}. Select one news item. Return JSON only.",
        tools=[{"type": "web_search_20250305"}],
    )
    # Extract JSON from response
    m = re.search(r'\{[^{}]+\}', result, re.DOTALL)
    if not m:
        raise ValueError(f"curator returned no JSON:\n{result}")
    return json.loads(m.group())


def step_zen_retriever(summary: str, recently_used: list[str]) -> dict:
    """Find a matching ZEN or return not_found."""
    zen_index = (KNOWLEDGE_PATH / "zen_index.md").read_text()
    prompt = f"""News summary:
{summary}

Recently used ZEN (avoid these): {recently_used}

ZEN Index:
{zen_index}

Return JSON only."""
    result = call(
        system=load_system("zen_retriever"),
        user=prompt,
        model="claude-haiku-4-5-20251001",
    )
    m = re.search(r'\{[^{}]+\}', result, re.DOTALL)
    if not m:
        return {"zen_id": "not_found", "reason": "no JSON returned"}
    return json.loads(m.group())


def step_thinker(summary: str) -> dict:
    """Generate a new interpretation when no ZEN matches."""
    result = call(
        system=load_system("thinker"),
        user=f"News summary:\n{summary}\n\nWork through the thinking pipeline. Return JSON only.",
    )
    m = re.search(r'\{.*\}', result, re.DOTALL)
    if not m:
        raise ValueError(f"thinker returned no JSON:\n{result}")
    return json.loads(m.group())


def step_writer(news: dict, lens: dict, today: str) -> str:
    """Write the article body (no frontmatter)."""
    author_style = (ASSETS_PATH / "author_style.md").read_text()
    perspectives = (ASSETS_PATH / "perspectives.yaml").read_text()

    prompt = f"""Write a Japanese article using the following inputs.

## News
Title: {news['title']}
URL: {news['url']}
Summary: {news['summary']}

## Lens
{json.dumps(lens, ensure_ascii=False, indent=2)}

## Style reference
{author_style}

## Evaluation perspectives (use poetic/ironic lens)
{perspectives}

Return the article body only. No frontmatter. Japanese. 600–900 characters."""
    return call(system=load_system("writer"), user=prompt)


# ── Commands ──────────────────────────────────────────────────────────────────

def run_publish() -> None:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    recently_used = load_recently_used_zen()

    print(f"[1/4] curator — selecting news for {today}")
    news = step_curator(today)
    print(f"      → {news['title']}")

    print("[2/4] zen_retriever — finding lens")
    zen = step_zen_retriever(news["summary"], recently_used)

    if zen.get("zen_id") == "not_found":
        print(f"      → no match ({zen.get('reason', '')}). calling thinker.")
        print("[3/4] thinker — generating interpretation")
        think = step_thinker(news["summary"])
        lens = {"zen_id": "thinker_generated", **think}
    else:
        print(f"      → {zen['zen_id']}")
        lens = zen
        think = None

    print("[4/4] writer — drafting article")
    body = step_writer(news, lens, today)

    # Assemble frontmatter
    published = datetime.now(timezone.utc).isoformat(timespec="minutes")
    expires = (datetime.now(timezone.utc) + timedelta(days=30)).isoformat(timespec="minutes")
    frontmatter = f"""---
title: {news['title']}
published: {published}
expires: {expires}
zen_source: {lens['zen_id']}
source_url: {news['url']}
---

"""
    article = frontmatter + body.strip() + "\n"
    filename = slug(news["title"], published) + ".md"
    (ARTICLES_PATH / filename).write_text(article)
    print(f"Published: {filename}")

    # Append new ZEN candidate if thinker ran
    if think and "zen_candidate" in think:
        cand = think["zen_candidate"]
        with open(KNOWLEDGE_PATH / "zen_index.md", "a") as f:
            f.write(f"\n### ZEN-GENERATED ({today})\n")
            f.write(f"- cluster: {cand.get('cluster', 'unknown')}\n")
            f.write(f"- type: generated\n")
            f.write(f"- core: {cand.get('core', '')}\n")
            f.write(f"- activation_question: {cand.get('activation_question', '')}\n")
            f.write(f"- last_explored: {today}\n")
        print("ZEN candidate appended to zen_index.md")


def run_zen_cycle() -> None:
    """Deepen the oldest unexplored ZEN entry."""
    zen_index_path = KNOWLEDGE_PATH / "zen_index.md"
    zen_index = zen_index_path.read_text()

    blocks = zen_index.split("### ")
    target = None
    for block in blocks:
        if "last_explored: never" in block:
            m = re.match(r"(ZEN-\d+):", block)
            if m:
                target = (m.group(1), block)
                break

    if not target:
        print("All ZEN entries explored. Skipping.")
        return

    zen_id, block = target
    core = re.search(r"- core:\s*(.+)", block)
    aq = re.search(r"- activation_question:\s*(.+)", block)
    unresolved = re.search(r"- unresolved:\s*(.+)", block)

    prompt = f"""Deepen this ZEN entry by exploring its unresolved question.

ZEN: {zen_id}
Core: {core.group(1) if core else ''}
Activation question: {aq.group(1) if aq else ''}
Unresolved: {unresolved.group(1) if unresolved else ''}

Work through the thinking pipeline. Return a JSON zen_candidate that extends this entry."""

    result = call(system=load_system("thinker"), user=prompt)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Mark as explored
    updated = zen_index.replace("- last_explored: never\n", f"- last_explored: {today}\n", 1)
    # Append deep result
    zen_index_path.write_text(updated + f"\n---\n<!-- zen_deep: {zen_id} ({today}) -->\n{result}\n")
    print(f"ZEN cycle complete: {zen_id}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "publish"
    if cmd == "publish":
        run_publish()
    elif cmd == "reap":
        from ttl import reap
        reap()
    elif cmd == "zen":
        run_zen_cycle()
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
