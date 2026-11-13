# Chapter 21 — SQLite Database

SQLite एक lightweight local database है।

```bash
pkg install python
python
```

```python
import sqlite3
db = sqlite3.connect("learning.db")
db.execute("CREATE TABLE IF NOT EXISTS topics (name TEXT, done INTEGER)")
db.execute("INSERT INTO topics VALUES (?, ?)", ("Bash basics", 1))
db.commit()
for row in db.execute("SELECT name, done FROM topics"):
    print(row)
db.close()
```

SQL queries में values के लिए placeholders (`?`) इस्तेमाल करें; string जोड़कर SQL बनाना unsafe हो सकता है। Database backup रखें।
