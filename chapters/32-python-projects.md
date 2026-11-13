# Chapter 32 — Python Project Patterns

Python project को छोटे functions में बाँटें। User input validate करें और errors को readable बनाएं।

```python
def read_positive_number(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if value > 0:
                return value
        except ValueError:
            pass
        print("Positive number enter karein.")

print(read_positive_number("Number: "))
```

## अभ्यास
इसी pattern से quiz score या expense entry input validate करें।
