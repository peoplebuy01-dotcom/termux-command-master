# Chapter 07 — Processes और System Information

## System जानकारी
```bash
uname -a
whoami
date
df -h
du -sh ~
free -h
```
कुछ Android builds में `free` या कुछ proc जानकारी सीमित हो सकती है।

## Processes
```bash
ps
top
```
किसी process को रोकने से पहले उसका नाम और काम समझें। अपना चलाया हुआ test process रोकने के लिए ही शुरुआती अभ्यास करें।

## Disk usage
- `df -h`: filesystem में कुल/खाली जगह।
- `du -sh folder`: किसी folder का अनुमानित आकार।

## Battery और Android details
Android की जानकारी पाने के लिए उपलब्ध Termux:API package/add-on की जरूरत हो सकती है। केवल भरोसेमंद official source से add-on लें।

## अभ्यास
`df -h` और `du -sh ~` चलाकर storage usage की तुलना करें।
