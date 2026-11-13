# Operations Guide

## Recommended defensive workflow
1. Run `python tat.py audit --json audit.json` and review the baseline.
2. Run `python tat.py network --host your-approved-host.example` for DNS/HTTPS connectivity only.
3. Run `python tat.py webcheck https://your-domain.example --json web-review.json` only against a site you own or are authorized to review.
4. Run `python tat.py secret-scan ./your-project` before publishing code. Findings are redacted.
5. Create a baseline with `python tat.py hash-create ./important-folder --output baseline.json`.
6. Keep the manifest in a safe location separate from the folder being monitored. Re-run verification later.
7. Review logs locally with `python tat.py log-summary ./app.log`. Avoid sharing logs containing personal information.

## Interpreting results
- `OK`: the specific check completed without a detected issue.
- `REVIEW`: inspect the item manually; this is not automatically a vulnerability.
- `ERROR`: the check could not complete.

## Good practice
- Keep Termux and packages updated.
- Use a screen lock and device encryption.
- Keep backups of important files.
- Never put real API keys, passwords, or private keys in GitHub.
- Do not treat a clean scan as proof that a system is secure.
