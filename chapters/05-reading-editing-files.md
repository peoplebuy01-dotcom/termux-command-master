# Chapter 05 — Files पढ़ना और Edit करना

## पढ़ने के तरीके
```bash
cat notes.txt       # पूरी file दिखाएँ
less notes.txt      # page-wise पढ़ें; q से बाहर
head notes.txt      # पहली 10 lines
tail notes.txt      # आखिरी 10 lines
wc -l notes.txt     # lines की संख्या
file notes.txt      # file type का अनुमान
```

## Text लिखना
```bash
echo "First line" > notes.txt
echo "Second line" >> notes.txt
```

## Editor
`nano` install करके file edit कर सकते हैं:
```bash
pkg install nano
nano notes.txt
```
Nano में Ctrl+O save, Enter confirm और Ctrl+X exit।

## Search
```bash
grep "Second" notes.txt
grep -n "line" notes.txt
```

## Common errors
- File नहीं मिले: `pwd` और `ls` से location जाँचें।
- Permission denied: file ownership/location देखें; बिना समझे root access न लें।

## अभ्यास
तीन lines लिखें और `grep`, `wc`, `head` से जाँचें।
