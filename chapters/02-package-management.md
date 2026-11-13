# Chapter 02 — Package Manager: pkg और apt

## Package क्या है?
Package पहले से तैयार software होता है। Termux में `pkg` आसान wrapper है और `apt` Debian package manager है।

## जरूरी commands
```bash
pkg update                 # package list refresh
pkg upgrade                # installed packages update
pkg search python          # package खोजें
pkg show python            # package details
pkg install python         # Python install
pkg uninstall python       # package हटाएँ
pkg list-installed         # installed packages
```

## सुरक्षित workflow
पहले `pkg update`, फिर जरूरत के अनुसार `pkg upgrade`। किसी random वेबसाइट से APK या shell installer डाउनलोड करने के बजाय official repositories को प्राथमिकता दें।

## उदाहरण
```bash
pkg install git
git --version
```

## Troubleshooting
- Mirror error आए तो Termux repository/mirror settings जाँचें।
- Storage कम हो तो अनावश्यक packages हटाएँ।
- पुराने Play Store builds में package समस्याएँ आ सकती हैं; official current Termux source इस्तेमाल करें।

## अभ्यास
`git` और `python` install करें, फिर version commands से जाँचें।
