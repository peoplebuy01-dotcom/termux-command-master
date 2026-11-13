# Termux Command Reference — Starter Pack

यह शुरुआती reference है। Commands की availability installed packages और Android version के अनुसार बदल सकती है।

| Command | काम |
|---|---|
| `pwd` | current folder |
| `ls -la` | files और hidden files |
| `cd folder` | folder बदलना |
| `mkdir -p path` | folder बनाना |
| `touch file` | खाली file बनाना |
| `cp a b` | copy |
| `mv a b` | move/rename |
| `rm file` | file हटाना |
| `cat file` | file पढ़ना |
| `less file` | page-wise पढ़ना |
| `head file` | शुरुआती lines |
| `tail file` | आखिरी lines |
| `grep word file` | text खोज |
| `find . -name '*.txt'` | नाम से file खोज |
| `wc -l file` | line count |
| `echo text` | text print |
| `date` | date/time |
| `whoami` | current user |
| `uname -a` | system/kernel info |
| `df -h` | disk space |
| `du -sh folder` | folder size |
| `ps` | processes |
| `top` | live process view |
| `chmod` | permissions बदलना |
| `which command` | executable path |
| `command -v command` | command lookup |
| `pkg update` | package list update |
| `pkg upgrade` | packages upgrade |
| `pkg search name` | package search |
| `pkg install name` | package install |
| `pkg uninstall name` | package remove |
| `git status` | Git status |
| `git add file` | stage changes |
| `git commit -m "msg"` | commit |
| `git log --oneline` | commit history |
| `python --version` | Python version |
| `python file.py` | Python script |
| `bash file.sh` | Bash script |
| `tar -czf out.tar.gz folder` | tar gzip archive |
| `unzip -l file.zip` | zip contents |
| `curl -I https://example.com` | HTTP headers |
| `nslookup example.com` | DNS lookup |
| `clear` | terminal साफ |
| `history` | command history |
| `man ls` | manual (अगर उपलब्ध) |
| `nano file` | text editor |
| `sleep 2` | 2 seconds wait |
| `printf` | formatted output |
| `sort file` | lines sort |
| `uniq file` | adjacent duplicate lines हटाना |

## Delete से पहले
`rm` सामान्यतः recycle bin में नहीं भेजता। पहले `pwd` और `ls` से location जाँचें। Wildcards और recursive delete का अभ्यास केवल disposable test folder में करें।
