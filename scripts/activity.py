"""Append explicitly automated, current-date activity commits."""
import datetime
import json
from pathlib import Path
import secrets
import subprocess


def git(*args):
    subprocess.run(["git", *args], check=True)


def main():
    count = secrets.randbelow(3) + 1
    path = Path("activity.jsonl")
    for index in range(count):
        entry = {
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "kind": "automated-activity",
            "entry": index + 1,
            "entries_in_run": count,
            "id": secrets.token_hex(8),
        }
        with path.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(entry) + "\n")
        git("add", "activity.jsonl")
        git("commit", "-m", f"chore: automated activity entry {index + 1}/{count}")


if __name__ == "__main__":
    main()
