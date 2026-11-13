# Termux Command Master

**Termux सीखें: Zero से Advanced तक — आसान हिंदी और English में।**

यह repository Android पर Termux terminal सीखने वालों के लिए एक practical learning guide है। इसका लक्ष्य commands को केवल list करना नहीं, बल्कि उनका सही उपयोग, संभावित output, common errors और safety समझाना है।

## किसके लिए?

- बिल्कुल नए Termux users
- Android पर Linux commands सीखने वाले विद्यार्थी
- Shell scripting और automation की शुरुआत करने वाले लोग
- अपने Android device पर सुरक्षित, वैध और उपयोगी projects बनाने वाले learners

## Learning roadmap

इस repository का planned syllabus 35 chapters में बाँटा गया है:

1. Termux installation और first setup
2. Package manager: pkg और apt
3. Files और directories
4. File create, copy, move और delete
5. Reading और editing files
6. Users, permissions और storage
7. Process और system information
8. Networking fundamentals
9. SSH और remote access (अपने devices/accounts पर)
10. Git और GitHub
11. Bash basics
12. Variables, conditions और loops
13. Functions और scripts
14. Python in Termux
15. Useful Python packages
16. Text processing
17. Archives और backups
18. Task automation
19. Local web servers
20. APIs की सुरक्षित basics
21. Databases
22. Android- और Termux-specific workflows
23. Debugging और troubleshooting
24. Performance और storage management
25. Privacy और security hygiene
26. Safe networking diagnostics
27. Authorized security-learning lab concepts
28. Developer tools
29. Project structure और documentation
30. Git collaboration
31. Shell scripting projects
32. Python projects
33. Personal productivity tools
34. Backup और file-management projects
35. Final practical projects

> यह roadmap है; सभी chapters और projects अभी पूर्ण विस्तार में उपलब्ध हों, यह जरूरी नहीं। सामग्री चरणबद्ध तरीके से जोड़ी जाएगी।

## Command lesson format

जहाँ लागू होगा, हर command lesson में ये बातें शामिल होंगी:

- Command और उसका उद्देश्य
- Syntax
- Example
- Expected output या output का अर्थ
- Real-world use
- Common errors और fixes
- Android/Termux compatibility notes
- Safety warning, जहाँ जरूरी हो

## Quick start

Termux खोलकर package list update करें:

```bash
pkg update && pkg upgrade
```

मदद के लिए:

```bash
pkg help
man ls
```

कुछ commands के लिए संबंधित package install करना पड़ सकता है। हर Linux command हर Android/Termux version पर समान रूप से उपलब्ध नहीं होती।

## Safety rules

- Commands को समझकर चलाएँ; अनजान scripts को सीधे execute न करें।
- `rm -rf`, root access और storage permissions का उपयोग बहुत सावधानी से करें।
- केवल अपने devices, accounts और systems पर testing करें या स्पष्ट अनुमति लें।
- Password, API key, access token और निजी जानकारी GitHub पर commit न करें।
- किसी भी security lesson का उपयोग unauthorized access, नुकसान या privacy violation के लिए न करें।

## Contributing

Typo fix, clearer explanation, tested example या नया beginner-friendly lesson योगदान करने के लिए [CONTRIBUTING.md](CONTRIBUTING.md) देखें। हर command को वास्तविक Termux environment में test करके version/limitations लिखें।

## Project status

यह learning project active development में है। पहले foundational guides, फिर detailed chapters और complete practical projects जोड़े जाएँगे। अधूरी सामग्री को complete बताने के बजाय उसकी स्थिति स्पष्ट रखी जाएगी।

## License

इस repository की सामग्री MIT License के अंतर्गत उपलब्ध है। विवरण के लिए [LICENSE](LICENSE) देखें।
