# autonomous-publisher

A self-running publishing system. Every day it selects one piece of news, finds a philosophical lens to read it through, writes a short Japanese article, and publishes it here. Articles expire after 30 days and are automatically deleted.

The system grows its own knowledge base. When no existing lens applies, it generates a new one.

---

## What it does

```
09:00 UTC daily
  curator    → selects today's most structurally interesting news item
  zen_retriever → searches the ZEN index for a matching philosophical lens
  thinker    → if no lens found: generates a new interpretation + ZEN candidate
  writer     → produces a short Japanese article (600–900 chars)
  → committed to articles/

every 6 hours
  zen_worker → deepens the oldest unexplored ZEN entry
  → committed to knowledge/zen_index.md

01:00 UTC daily
  reaper     → deletes articles older than 30 days
```

---

## Architecture

- **Agents**: defined in `agents/`. Each has a single responsibility.
- **Knowledge**: `knowledge/zen_index.md` — a seeded philosophical knowledge base that grows as the system runs.
- **Assets**: `assets/author_style.md` and `assets/perspectives.yaml` — writing style constraints.
- **Articles**: `articles/` — live articles with TTL frontmatter. Max ~30 at any time.

Built with [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview).

---

## Run locally

```bash
export ANTHROPIC_API_KEY=sk-...
pip install anthropic
cd src
python main.py publish   # generate today's article
python main.py zen       # run one ZEN cycle
python main.py reap      # delete expired articles
```

---

## Design notes

The system does not optimize for engagement. It optimizes for a specific quality:
words that read as virtue while simultaneously functioning as critique.

The 30-day expiry is not a technical constraint. It is a design decision.
What stays is what the system chose to keep thinking about.
