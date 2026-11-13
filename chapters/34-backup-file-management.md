# Chapter 34 — Backup और File Management

## 3-2-1 principle
महत्वपूर्ण data की 3 copies, 2 अलग media पर और 1 copy अलग स्थान पर रखना अच्छा लक्ष्य है।

## Verify archive
```bash
tar -tzf backup.tar.gz | head
```

Restore से पहले अलग test folder में extract करें। Backup तभी उपयोगी है जब restore करके verify किया जा सके। Cloud backup में account security और privacy भी देखें।
