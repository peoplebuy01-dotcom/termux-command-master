# Chapter 20 — Python Functions और Errors

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Zero se divide nahi kar sakte")
    return a / b

try:
    print(divide(10, 2))
except ValueError as error:
    print("Input error:", error)
```

Function reusable code block है। `try/except` expected errors को संभालता है। हर exception को चुपचाप ignore न करें; user को स्पष्ट संदेश दें।

## अभ्यास
एक function बनाएँ जो दो numbers का average लौटाए और empty input को संभाले।
