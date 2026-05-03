"""ZEN index search utilities."""
import re
from pathlib import Path
from datetime import date, timedelta

ZEN_INDEX_PATH = Path(__file__).parent.parent / "knowledge" / "zen_index.md"
ARTICLES_PATH = Path(__file__).parent.parent / "articles"


def load_recently_used_zen(days: int = 30) -> list[str]:
    """Return ZEN IDs used in articles published within the last `days` days."""
    cutoff = date.today() - timedelta(days=days)
    used = []
    for article in ARTICLES_PATH.glob("*.md"):
        if article.name == ".gitkeep":
            continue
        content = article.read_text()
        m = re.search(r"zen_source:\s*(ZEN-\d+)", content)
        pub = re.search(r"published:\s*(\d{4}-\d{2}-\d{2})", content)
        if m and pub:
            pub_date = date.fromisoformat(pub.group(1))
            if pub_date >= cutoff:
                used.append(m.group(1))
    return used


def load_zen_titles() -> dict[str, str]:
    """Return {zen_id: first line of core} for display purposes."""
    text = ZEN_INDEX_PATH.read_text()
    entries = {}
    for block in text.split("### "):
        m = re.match(r"(ZEN-\d+):", block)
        if m:
            core_m = re.search(r"- core:\s*(.+)", block)
            if core_m:
                entries[m.group(1)] = core_m.group(1)[:80]
    return entries
