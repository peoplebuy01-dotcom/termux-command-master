# Chapter 16 — Text Processing

## सीखें
`grep` text खोजता है, `sort` lines क्रम में लगाता है, `uniq` लगातार duplicate lines हटाता है और `cut` columns निकालता है।

```bash
printf "apple\nbanana\napple\n" > fruits.txt
grep -n "apple" fruits.txt
sort fruits.txt
sort fruits.txt | uniq
cut -d: -f1 /etc/passwd
```

## Pipe
`command1 | command2` पहले command का output अगले command को देता है।

## अभ्यास
अपनी बनाई हुई text file में कोई शब्द खोजें और lines sort करें। निजी system files का data सार्वजनिक न करें।
