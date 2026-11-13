# Chapter 19 — Python Files और JSON

```python
import json
from pathlib import Path

data = {"topic": "Termux", "completed": False}
path = Path("progress.json")
path.write_text(json.dumps(data, indent=2), encoding="utf-8")
loaded = json.loads(path.read_text(encoding="utf-8"))
print(loaded["topic"])
```

Files के लिए `with open(...)` भी उपयोग कर सकते हैं। JSON में strings, numbers, booleans, lists और dictionaries रखे जा सकते हैं।

## अभ्यास
अपनी learning progress को JSON file में save और फिर read करें। Password जैसी secret जानकारी plain JSON में न रखें।
