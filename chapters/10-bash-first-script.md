# Chapter 10 — Bash और पहला Script

## Script क्या है?
Shell script commands की file होती है, जिसे क्रम से चलाया जाता है।

## पहला script
```bash
mkdir -p ~/termux-learning
cd ~/termux-learning
cat > hello.sh <<'EOF'
#!/data/data/com.termux/files/usr/bin/bash
echo "Namaste! Termux ready hai."
echo "Aaj ki date: $(date)"
EOF
chmod +x hello.sh
./hello.sh
```

## समझें
- Shebang पहली line बताती है कि script किस interpreter से चले।
- `echo` text दिखाता है।
- `$(date)` command substitution है।
- `chmod +x` execute permission देता है।

## Debug
```bash
bash -n hello.sh
bash -x hello.sh
```
पहला syntax जाँचता है; दूसरा commands को trace करता है।

## अभ्यास
Script में अपना पसंदीदा learning topic print करें। निजी जानकारी script में न रखें।
