# Chapter 01 — Termux Installation और First Setup

## लक्ष्य
Termux Android पर Linux-जैसा terminal environment देता है। यह पूरा Linux desktop नहीं है; Android की permissions और battery restrictions लागू रहती हैं।

## Installation
1. F-Droid या Termux के official GitHub releases जैसे भरोसेमंद स्रोत से Termux लें।
2. अलग-अलग स्रोतों के Termux और add-on apps को mix न करें।
3. पहली बार खोलकर repositories update करें:

```bash
pkg update
pkg upgrade
```

## पहला परिचय
```bash
whoami       # वर्तमान user
pwd          # वर्तमान folder
uname -a     # kernel/system जानकारी
date         # तारीख और समय
```

## Output कैसे पढ़ें?
`pwd` आम तौर पर Termux home directory दिखाता है। Termux में सामान्य home path `/data/data/com.termux/files/home` होता है।

## Common errors
- **Repository unavailable:** इंटरनेट जाँचें और कुछ देर बाद `pkg update` दोबारा चलाएँ।
- **Command not found:** package install करना पड़ सकता है।
- **Permission denied:** Android/Termux permissions और file location जाँचें।

## अभ्यास
`pwd`, `whoami`, `date` चलाएँ और उनके output का अर्थ अपनी notebook में लिखें।
