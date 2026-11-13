# TAT Pro — Termux Advanced Cyber Defense Suite

A modular, defensive cybersecurity toolkit designed for Termux and Python 3. It focuses on **systems you own or have explicit permission to assess**.

## Features
- System baseline audit: OS/Python/storage basics and selected risky file-permission checks.
- Network diagnostics: DNS resolution, default-route information and connectivity checks (no port scanning).
- Website security review: HTTPS/TLS certificate metadata and common HTTP security headers.
- File integrity: SHA-256 manifest creation and verification.
- Log triage: summarize common error/authentication-failure patterns from a log file.
- JSON reports, clear errors, offline-friendly core, and a modular structure.

## Safety boundary
This project is for defensive learning and authorized administration. It does not include exploitation, credential attacks, stealth, persistence, malware, or unauthorized scanning. Only test websites and devices you own or are explicitly allowed to assess. Do not upload private logs or integrity manifests publicly.

## Requirements
- Android with Termux
- Python 3.10+
- Optional: Termux:API for extra Android integration (not required by this version)

## Install
```bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/peoplebuy01-dotcom/termux-command-master.git
cd termux-command-master/advanced-cyber-defense-suite
python tat.py
```

Run a module:
```bash
python tat.py audit
python tat.py network
python tat.py webcheck https://example.com
python tat.py hash-create ./my-folder --output integrity.json
python tat.py hash-verify ./my-folder --manifest integrity.json
python tat.py log-summary ./sample.log
```

## Output
Reports are printed in the terminal. Use `--json report.json` on supported commands to save machine-readable output.

## Project layout
- `tat.py`: command-line entry point
- `tatlib/`: independent modules
- `tests/`: standard-library tests
- `docs/`: learning and operational guidance

## Important limitations
- Android restricts access to many system areas; the audit reports only what Termux can legitimately read.
- Network checks are limited to DNS and basic connectivity; there is no network discovery or port scanning.
- HTTP checks make a normal GET request to the exact URL supplied. Use only an authorized target.
- Log analysis is heuristic and does not prove an intrusion occurred.

## Tests
```bash
python -m unittest discover -s tests -v
```

## License
MIT. See [LICENSE](LICENSE).
