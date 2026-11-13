# Chapter 31 — Shell Project Patterns

एक सुरक्षित shell script में:
- सही shebang
- quoted variables
- input validation
- clear error messages
- backup/dry-run जहाँ files बदलती हों
- exit status

उदाहरण:
```bash
#!/data/data/com.termux/files/usr/bin/bash
set -eu
target="$HOME/termux-learning"
if [ -d "$target" ]; then
  printf 'Folder exists: %s\n' "$target"
else
  printf 'Folder not found\n' >&2
  exit 1
fi
```

इसे अपने test folder में चलाकर देखें।
