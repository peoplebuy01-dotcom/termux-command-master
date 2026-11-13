# Chapter 23 — Debugging और Logs

## छोटे diagnostic steps
```bash
command -v python
python --version
pwd
ls -la
bash -n script.sh
```

## Script trace
```bash
bash -x script.sh
```

Error message की पहली और आखिरी lines के साथ command और environment note करें। Logs साझा करने से पहले tokens, usernames, private URLs और personal data हटा दें।

## अभ्यास
अपने script में syntax mistake डालें, `bash -n` से पहचानें और सुधारें।
