"""Local, read-only scan for common accidentally committed secret patterns.
Values are never printed; only file, line and finding type are reported."""
from pathlib import Path
import re

RULES = {
    "private_key_block": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "generic_api_token": re.compile(r"(?i)(api[_-]?key|access[_-]?token|client[_-]?secret)\s*[:=]\s*['\"][A-Za-z0-9_./+=-]{12,}['\"]"),
    "cloud_access_key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "github_token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
}


def scan_directory(directory):
    root = Path(directory).expanduser().resolve()
    if not root.is_dir():
        raise ValueError("Directory does not exist.")
    findings = []
    skipped = 0
    for path in root.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        if any(part in {".git", ".venv", "venv", "__pycache__", "node_modules"} for part in path.parts):
            skipped += 1
            continue
        try:
            if path.stat().st_size > 2_000_000:
                skipped += 1
                continue
            content = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            skipped += 1
            continue
        for number, line in enumerate(content.splitlines(), 1):
            for kind, pattern in RULES.items():
                if pattern.search(line):
                    findings.append({"file": str(path.relative_to(root)), "line": number,
                                     "type": kind, "value": "[REDACTED]"})
    return {"tool": "TAT Pro", "module": "local-secret-hygiene", "read_only": True,
            "finding_count": len(findings), "findings": findings, "skipped_files": skipped,
            "note": "Pattern matches can be false positives. Rotate any real exposed credential; do not paste it into reports."}
