def calculate(a: float, operator: str, b: float) -> float:
    if operator == "+": return a + b
    if operator == "-": return a - b
    if operator == "*": return a * b
    if operator == "/":
        if b == 0:
            raise ValueError("Zero se divide nahi kar sakte.")
        return a / b
    raise ValueError("Operator +, -, * ya / hona chahiye.")

try:
    first = float(input("First number: "))
    op = input("Operator (+ - * /): ").strip()
    second = float(input("Second number: "))
    print("Result:", calculate(first, op, second))
except ValueError as error:
    print("Input error:", error)
