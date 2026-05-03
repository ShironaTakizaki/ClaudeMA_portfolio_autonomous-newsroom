"""TTL management: find and delete expired articles."""
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ARTICLES_PATH = Path(__file__).parent.parent / "articles"


def find_expired() -> list[Path]:
    now = datetime.now(timezone.utc)
    expired = []
    for article in ARTICLES_PATH.glob("*.md"):
        if article.name == ".gitkeep":
            continue
        content = article.read_text()
        m = re.search(r"expires:\s*(\S+)", content)
        if not m:
            continue
        try:
            exp = datetime.fromisoformat(m.group(1).rstrip("Z")).replace(tzinfo=timezone.utc)
            if exp <= now:
                expired.append(article)
        except ValueError:
            continue
    return expired


def reap(dry_run: bool = False) -> int:
    expired = find_expired()
    for path in expired:
        print(f"{'[dry-run] ' if dry_run else ''}Deleting: {path.name}")
        if not dry_run:
            path.unlink()
    return len(expired)


if __name__ == "__main__":
    dry = "--dry-run" in sys.argv
    count = reap(dry_run=dry)
    print(f"Reaped {count} article(s).")
