# Chapter 04 — File Create, Copy, Move और Delete

## Commands
```bash
touch notes.txt                 # खाली file
cp notes.txt notes-backup.txt   # copy
mv notes-backup.txt backup.txt  # rename/move
rm backup.txt                   # file delete
mkdir archive                   # folder
cp notes.txt archive/           # folder में copy
```

## सावधानी
Delete command सामान्यतः Trash में नहीं भेजती। `rm -r` directories और उनके अंदर की सामग्री हटा सकता है। `rm -rf` को सीखने के शुरुआती अभ्यास में इस्तेमाल न करें।

## सुरक्षित अभ्यास
```bash
mkdir -p safe-practice
cd safe-practice
echo "Hello Termux" > hello.txt
cp hello.txt hello-copy.txt
cat hello-copy.txt
```

## Redirect
- `>` file को overwrite करता है।
- `>>` file के अंत में जोड़ता है।
- `|` एक command का output दूसरी command को देता है।

## अभ्यास
एक file बनाएँ, उसकी copy बनाएँ, copy का नाम बदलें और केवल copy हटाएँ।
