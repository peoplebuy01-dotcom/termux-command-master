import json
from pathlib import Path
from datetime import datetime

path = Path.home() / "termux-progress.json"
topic = input("Aaj ka completed topic: ").strip()
if not topic:
    raise SystemExit("Topic khali nahi ho sakta.")

entries = []
if path.exists():
    try:
        entries = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(entries, list):
            raise ValueError("Progress file list format mein nahi hai.")
    except (json.JSONDecodeError, ValueError) as error:
        raise SystemExit(f"Existing progress file read nahi hui: {error}")

entries.append({"date": datetime.now().isoformat(timespec="minutes"), "topic": topic})
path.write_text(json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Saved {len(entries)} entries to {path}")
