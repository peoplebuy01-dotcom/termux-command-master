# Chapter 03 — Files और Directories

## रास्ता (path)
- Absolute path: root से पूरा रास्ता, जैसे `/data/data/com.termux/files/home`
- Relative path: current folder के मुकाबले रास्ता, जैसे `Documents/notes`

## Commands
```bash
pwd                 # current directory
ls                  # files देखें
ls -la              # hidden files सहित details
cd                  # home जाएँ
cd ..               # parent folder
mkdir practice      # folder बनाएँ
mkdir -p a/b/c      # nested folders
rmdir empty-folder  # खाली folder हटाएँ
```

## उदाहरण
```bash
mkdir -p practice/day1
cd practice/day1
pwd
```

## Hidden files
Linux में dot से शुरू नाम hidden होते हैं। `ls -la` उन्हें दिखाता है।

## Common mistakes
- Folder name में spaces हों तो quotes लगाएँ: `cd "My Notes"`
- `cd` अकेले चलाने से home directory खुलती है।
- `rmdir` केवल खाली directory हटाता है।

## अभ्यास
`learning/week1` नाम का folder बनाएँ और उसमें जाएँ।
