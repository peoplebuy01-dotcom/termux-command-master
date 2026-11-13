# Chapter 11 — Bash Variables, Conditions और Loops

## Variables
```bash
name="Learner"
echo "Hello, $name"
```
Assignment में `=` के आसपास spaces नहीं होते।

## Condition
```bash
if [ -f notes.txt ]; then
  echo "File exists"
else
  echo "File missing"
fi
```

## Loop
```bash
for item in one two three; do
  echo "$item"
done
```

## User input
```bash
read -r -p "Apna topic likho: " topic
printf 'Topic: %s\n' "$topic"
```

## अच्छी आदतें
Variables को quotes में रखें: `"$name"`। इससे spaces वाले नामों में errors कम होते हैं। अनजान input को सीधे shell command के रूप में execute न करें।

## अभ्यास
एक script बनाएँ जो file मौजूद है या नहीं बताती है।
