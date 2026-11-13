# Architecture

TAT Pro is intentionally dependency-free and separates the command-line interface from its modules.

- `tat.py`: argument parsing, dispatch and report output.
- `tatlib/audit.py`: read-only Termux-visible baseline.
- `tatlib/network.py`: DNS lookup and a single HTTPS HEAD connectivity request.
- `tatlib/webcheck.py`: HTTPS request and security-header review.
- `tatlib/integrity.py`: streaming SHA-256 hashing and manifest verification.
- `tatlib/logs.py`: local heuristic log classification.
- `tatlib/secretscan.py`: local pattern matching with redacted findings.
- `tests/`: unit tests using Python's standard library.

## Design principles
1. Read-only inspection wherever possible.
2. No secret values in scanner output.
3. Explicit target input for web checks.
4. No broad network scanning or exploit functionality.
5. Standard-library implementation to reduce supply-chain risk.
6. Findings are evidence for human review, not definitive security verdicts.
