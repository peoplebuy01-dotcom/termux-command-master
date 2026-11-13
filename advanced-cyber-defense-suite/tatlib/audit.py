"""Read-only baseline checks that work within Termux permissions."""
import os
import platform
import shutil
import sys
from pathlib import Path


def run_audit():
    home = Path.home()
    disk = shutil.disk_usage(str(home))
    checks = []
    def add(name, status, detail):
        checks.append({"check": name, "status": status, "detail": str(detail)})

    add("platform", "INFO", platform.platform())
    add("python", "INFO", sys.version.split()[0])
    add("home_directory", "INFO", home)
    add("home_permissions", "INFO", oct(home.stat().st_mode & 0o777))
    add("storage_total_bytes", "INFO", disk.total)
    add("storage_used_bytes", "INFO", disk.used)
    add("storage_free_bytes", "INFO", disk.free)

    for candidate in (home / ".ssh", home / ".config"):
        if candidate.exists():
            mode = candidate.stat().st_mode & 0o777
            status = "REVIEW" if mode & 0o077 else "OK"
            add(f"{candidate.name}_permissions", status, f"{oct(mode)}; review if sensitive files are stored here")

    env_flags = [key for key in os.environ if any(word in key.lower() for word in ("token", "secret", "password", "api_key"))]
    add("sensitive_environment_variable_names", "REVIEW" if env_flags else "OK",
        ", ".join(sorted(env_flags)) if env_flags else "No obvious secret-like variable names found")
    return {"tool": "TAT Pro", "module": "system-audit", "read_only": True, "checks": checks,
            "note": "Termux cannot inspect all Android system settings; this is not a complete device security certification."}
