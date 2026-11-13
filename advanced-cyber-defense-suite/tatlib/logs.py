"""Heuristic local log triage; findings require human review."""
from collections import Counter
from pathlib import Path
import re

PATTERNS = {
    "error": re.compile(r"\b(error|failed|failure|exception)\b", re.I),
    "authentication_failure": re.compile(r"(authentication failed|login failed|invalid password|unauthorized)", re.I),
    "permission_denied": re.compile(r"(permission denied|access denied)", re.I),
    "warning": re.compile(r"\bwarning\b", re.I),
}


def summarize_log(filename):
    path = Path(filename).expanduser()
    if not path.is_file():
        raise ValueError("Log file does not exist.")
    counts = Counter()
    samples = {key: [] for key in PATTERNS}
    total = 0
    with path.open("r", encoding="utf-8", errors="replace") as stream:
        for line_number, line in enumerate(stream, 1):
            total += 1
            for label, pattern in PATTERNS.items():
                if pattern.search(line):
                    counts[label] += 1
                    if len(samples[label]) < 3:
                        samples[label].append({"line": line_number, "text": line.strip()[:240]})
    return {"tool": "TAT Pro", "module": "log-triage", "file": str(path),
            "total_lines": total, "counts": dict(counts), "sample_matches": samples,
            "note": "Patterns are heuristic indicators, not proof of compromise. Review logs locally and protect personal data."}
