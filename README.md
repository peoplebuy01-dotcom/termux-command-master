# Termux Command Master

**Termux सीखें: Zero से Advanced तक — आसान हिंदी और English में।**

यह Android पर Termux सीखने वालों के लिए practical, beginner-friendly guide है। हर lesson में उद्देश्य, command examples, common errors, practice और safety notes दिए गए हैं।

## शुरुआत कहाँ से करें?

1. [Chapter 01 — Termux Installation](chapters/01-termux-installation.md)
2. [Chapter 02 — Package Manager](chapters/02-package-management.md)
3. [Chapter 03 — Files और Directories](chapters/03-files-and-directories.md)
4. [Chapter 04 — File Operations](chapters/04-file-operations.md)
5. [Chapter 05 — Reading और Editing Files](chapters/05-reading-editing-files.md)

इसके बाद chapters को क्रम से पढ़ें। [पूरी Command Reference](COMMAND-REFERENCE.md) और [10 Practical Projects](PROJECTS.md) भी उपलब्ध हैं।

## सभी 35 Chapters

| # | विषय | अध्याय |
|---|---|---|
| 01 | Installation और first setup | [खोलें](chapters/01-termux-installation.md) |
| 02 | pkg और apt | [खोलें](chapters/02-package-management.md) |
| 03 | Files और directories | [खोलें](chapters/03-files-and-directories.md) |
| 04 | Create, copy, move, delete | [खोलें](chapters/04-file-operations.md) |
| 05 | Reading और editing | [खोलें](chapters/05-reading-editing-files.md) |
| 06 | Storage और permissions | [खोलें](chapters/06-storage-permissions.md) |
| 07 | Processes और system info | [खोलें](chapters/07-process-system-info.md) |
| 08 | Networking basics | [खोलें](chapters/08-networking-basics.md) |
| 09 | Git और GitHub | [खोलें](chapters/09-git-github.md) |
| 10 | Bash first script | [खोलें](chapters/10-bash-first-script.md) |
| 11 | Variables, conditions, loops | [खोलें](chapters/11-bash-variables-conditions-loops.md) |
| 12 | Python in Termux | [खोलें](chapters/12-python-in-termux.md) |
| 13 | Archives और backups | [खोलें](chapters/13-archives-backups.md) |
| 14 | Local web server | [खोलें](chapters/14-local-web-server.md) |
| 15 | Troubleshooting | [खोलें](chapters/15-troubleshooting.md) |
| 16 | Text processing | [खोलें](chapters/16-text-processing.md) |
| 17 | Automation basics | [खोलें](chapters/17-automation-and-scheduling.md) |
| 18 | APIs और curl | [खोलें](chapters/18-apis-and-curl.md) |
| 19 | Python files और JSON | [खोलें](chapters/19-python-files-json.md) |
| 20 | Python functions और errors | [खोलें](chapters/20-python-functions-errors.md) |
| 21 | SQLite database | [खोलें](chapters/21-databases-sqlite.md) |
| 22 | Android Termux:API | [खोलें](chapters/22-android-termux-api.md) |
| 23 | Debugging और logs | [खोलें](chapters/23-debugging-logs.md) |
| 24 | Performance और storage | [खोलें](chapters/24-performance-storage.md) |
| 25 | Privacy और security | [खोलें](chapters/25-privacy-security-hygiene.md) |
| 26 | Safe network diagnostics | [खोलें](chapters/26-safe-network-diagnostics.md) |
| 27 | Authorized security learning | [खोलें](chapters/27-authorized-security-learning.md) |
| 28 | Developer tools | [खोलें](chapters/28-developer-tools.md) |
| 29 | Project structure और docs | [खोलें](chapters/29-project-structure-docs.md) |
| 30 | Git collaboration | [खोलें](chapters/30-git-collaboration.md) |
| 31 | Shell project patterns | [खोलें](chapters/31-shell-projects.md) |
| 32 | Python project patterns | [खोलें](chapters/32-python-projects.md) |
| 33 | Productivity tools | [खोलें](chapters/33-productivity-tools.md) |
| 34 | Backup और file management | [खोलें](chapters/34-backup-file-management.md) |
| 35 | Capstone projects | [खोलें](chapters/35-capstone-projects.md) |

## Practical projects

हर project का code [projects/](projects/) folder में है:

1. [Notes Manager](projects/01-notes-manager/notes.sh)
2. [Daily Learning Log](projects/02-daily-learning-log/log.sh)
3. [Backup Creator](projects/03-backup-creator/backup.sh)
4. [Disk Usage Report](projects/04-disk-report/report.sh)
5. [File Organizer — safe dry-run](projects/05-file-organizer/organize.py)
6. [Python Calculator](projects/06-python-calculator/calculator.py)
7. [Quiz App](projects/07-quiz-app/quiz.py)
8. [Local HTML Preview](projects/08-local-html-preview/index.html)
9. [Git Notes Practice](projects/09-git-notes/README.md)
10. [JSON Progress Tracker](projects/10-json-progress/progress.py)

## Command Reference

[Starter Command Reference खोलें](COMMAND-REFERENCE.md)। यह अभी foundational list है; इसे आगे बढ़ाकर हर command के syntax, flags और compatibility notes जोड़े जाएँगे।

## Termux Quick Start

```bash
pkg update
pkg upgrade
pkg install git python nano
```

कुछ commands के लिए अतिरिक्त package की जरूरत होती है। Android permissions और Termux version के कारण व्यवहार बदल सकता है।

## Safety first

- Commands को समझकर चलाएँ; random scripts को सीधे execute न करें।
- `rm`, recursive delete और permission changes से पहले path जाँचें।
- केवल अपने devices/accounts/systems या स्पष्ट अनुमति वाले environment पर testing करें।
- Password, API key और access token public repository में न डालें।
- Security content authorized, defensive learning तक सीमित है।

## Contributing और License

- [Contributing Guide](CONTRIBUTING.md)
- [Security Policy](SECURITY.md)
- [MIT License](LICENSE)

**Project status:** 35 chapter files और 10 beginner project files repository में जोड़े गए हैं। यह शुरुआती learning edition है; हर chapter को और विस्तार, screenshots और tested outputs के साथ बेहतर किया जा सकता है।