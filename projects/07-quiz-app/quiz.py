questions = [
    ("Termux kis platform par chalta hai?", "android"),
    ("Python file ka common extension kya hai?", ".py"),
    ("Git status command kya dikhata hai?", "working tree status"),
]
score = 0
for prompt, answer in questions:
    print("\n" + prompt)
    user_answer = input("> ").strip().lower()
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Answer:", answer)
print(f"\nScore: {score}/{len(questions)}")
