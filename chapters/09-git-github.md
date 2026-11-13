# Chapter 09 — Git और GitHub

## Git install
```bash
pkg install git
git --version
```

## Basic workflow
```bash
mkdir demo-repo
cd demo-repo
git init
echo "# Demo" > README.md
git status
git add README.md
git commit -m "Add README"
```

## Remote जोड़ना
अपनी बनाई हुई GitHub repository का URL लें:
```bash
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git branch -M main
git push -u origin main
```

## सुरक्षा
Password या personal access token को script, README या public repository में कभी न लिखें। GitHub का secure browser authentication/credential flow इस्तेमाल करें।

## Common errors
- `nothing to commit`: tracked file में बदलाव नहीं है।
- `remote origin already exists`: `git remote -v` देखें।
- Push rejected: पहले remote changes समझें; blindly force push न करें।

## अभ्यास
एक local repository बनाकर README commit करें।
