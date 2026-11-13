# Chapter 06 — Android Storage और Permissions

## Shared storage access
Termux में:
```bash
termux-setup-storage
```
Android permission prompt आए तो समझकर allow करें। इसके बाद सामान्यतः `~/storage/shared` shared storage का shortcut होता है।

## जाँचें
```bash
ls ~/storage
ls ~/storage/shared
```

## Permissions
```bash
ls -l script.sh
chmod +x script.sh
chmod 644 notes.txt
```
- `r`: read
- `w`: write
- `x`: execute/search

## महत्वपूर्ण सीमा
Android scoped storage और app sandbox के कारण हर system folder उपलब्ध नहीं होता। Root access के बिना protected Android app data पढ़ने की कोशिश न करें।

## अभ्यास
अपने shared storage में एक नया folder बनाएँ और उसमें test text file रखें।
