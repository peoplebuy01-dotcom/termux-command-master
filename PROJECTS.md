# 10 Practical Termux Projects

हर project को अपने फोन और अपनी files तक सीमित रखें। शुरुआत में test folder इस्तेमाल करें।

## 1. Personal Notes Manager
**सीखेंगे:** files, append, search। `mkdir -p ~/notes`, फिर `echo "idea" >> ~/notes/ideas.txt`; खोजने के लिए `grep -n "idea" ~/notes/ideas.txt`।

## 2. Daily Learning Log
**सीखेंगे:** date और redirection। `echo "$(date): आज Bash सीखा" >> ~/learning-log.txt`।

## 3. File Organizer (manual first)
**सीखेंगे:** `mkdir`, `mv`, extensions। पहले test folder में images/docs folders बनाकर sample files move करें। असली Downloads पर script चलाने से पहले dry-run और backup अनिवार्य रखें।

## 4. Backup Creator
**सीखेंगे:** tar, date। `tar -czf ~/backup-$(date +%F).tar.gz ~/termux-learning`।

## 5. Disk Usage Reporter
**सीखेंगे:** df, du। `df -h; du -sh ~`।

## 6. Bash Greeting Script
**सीखेंगे:** shebang, variables, command substitution। Chapter 10 का script बढ़ाकर date और current directory print करें।

## 7. Python Calculator
**सीखेंगे:** input, numeric conversion, conditions। केवल दो numbers और +, -, *, / operations लें; divide-by-zero को संभालें। `eval()` का उपयोग न करें।

## 8. Quiz Program
**सीखेंगे:** Python dictionaries, loops, score। अपने बनाए सामान्य ज्ञान के प्रश्न रखें और सही उत्तर पर score बढ़ाएँ।

## 9. Local HTML Preview
**सीखेंगे:** HTML और local server। Chapter 14 के अनुसार केवल localhost पर test करें।

## 10. Git Learning Repository
**सीखेंगे:** init, add, commit, log। अपने notes को Git repository में version-control करें; secrets commit न करें।

## Project checklist
- [ ] अलग test folder बनाया
- [ ] हर command समझी
- [ ] backup लिया जहाँ जरूरी था
- [ ] error messages पढ़े
- [ ] README में setup और usage लिखा
- [ ] कोई password/token शामिल नहीं किया
