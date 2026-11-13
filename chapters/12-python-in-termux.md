# Chapter 12 — Python in Termux

## Install और verify
```bash
pkg install python
python --version
```

## पहला program
```python
name = input("Aapka naam: ")
print(f"Namaste, {name}!")
```
इसे `hello.py` नाम से save करके चलाएँ:
```bash
python hello.py
```

## Python packages
Project के लिए virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install requests
```
काम पूरा होने पर `deactivate` चलाएँ।

## Common errors
- `python: command not found`: `pkg install python`
- Module missing: सही virtual environment activate करके package install करें।
- Permission/build errors: कुछ packages को Android पर native build support नहीं मिलता।

## अभ्यास
नाम पूछने और greeting print करने वाला छोटा program बनाएँ।
