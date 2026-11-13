# Chapter 17 — Automation Basics

Automation का मतलब दोहराए जाने वाले काम को script से करना है। पहले script को manually test करें।

## Example: daily log
```bash
#!/data/data/com.termux/files/usr/bin/bash
mkdir -p "$HOME/logs"
printf '%s - learning session\n' "$(date)" >> "$HOME/logs/daily.txt"
```

इसे `daily-log.sh` नाम से save करें और `bash daily-log.sh` चलाएँ।

## Scheduling
Android background restrictions के कारण सामान्य Linux cron हर फोन पर भरोसेमंद नहीं होता। जरूरत हो तो Termux:Boot/Termux:API की official documentation पढ़ें और battery optimization समझें। कोई भी script पहले manual test करें।
