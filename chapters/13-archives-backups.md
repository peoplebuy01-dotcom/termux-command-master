# Chapter 13 — Archives और Backups

## Zip utilities
```bash
pkg install zip unzip
zip -r project.zip project/
unzip -l project.zip
mkdir extracted
unzip project.zip -d extracted
```

## Backup क्यों?
गलत command, storage failure या accidental deletion से बचने के लिए महत्वपूर्ण files की दूसरी copy रखें।

## Simple dated backup
```bash
mkdir -p ~/backups
tar -czf ~/backups/home-backup-$(date +%F).tar.gz ~/termux-learning
```

## Restore से पहले
Archive की सूची देखें और किसी नए folder में extract करें। Existing files पर सीधे overwrite न करें।

## अभ्यास
एक test folder archive करें और अलग folder में extract करके files compare करें।
