# Chapter 15 — Troubleshooting और Debugging

## पहले ये जाँचें
```bash
pwd
ls -la
command -v python
python --version
pkg update
```

## आम errors
- **command not found:** command का नाम जाँचें; package खोजकर install करें।
- **permission denied:** path और permission जाँचें; अंधाधुंध `chmod 777` न करें।
- **no space left:** `df -h` और `du -sh` से storage देखें।
- **network/repository error:** इंटरनेट, DNS और repository status जाँचें।
- **script not executable:** interpreter से चलाएँ, जैसे `bash script.sh`, या उचित execute permission दें।

## Error report कैसे बनाएँ?
1. पूरी error message copy करें।
2. command और working directory लिखें।
3. Termux version और Android version बताएं।
4. Password, token, private IP या personal files का content साझा न करें।

## अभ्यास
जानबूझकर गलत command चलाएँ, error पढ़ें और कारण पहचानें।
