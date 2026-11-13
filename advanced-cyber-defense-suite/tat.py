#!/usr/bin/env python3
"""TAT Pro: defensive Termux toolkit. Python standard library only."""
import argparse
import json
import sys
from pathlib import Path

from tatlib.audit import run_audit
from tatlib.integrity import create_manifest, verify_manifest
from tatlib.network import run_network_checks
from tatlib.webcheck import check_website
from tatlib.logs import summarize_log


def emit(data, json_path=None):
    print(json.dumps(data, indent=2, ensure_ascii=False, default=str))
    if json_path:
        Path(json_path).write_text(json.dumps(data, indent=2, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
        print(f"\n[+] JSON report saved: {json_path}")


def main():
    parser = argparse.ArgumentParser(prog="tat", description="TAT Pro — defensive Termux toolkit")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("audit", help="Read-only system baseline audit")
    p.add_argument("--json", dest="json_path")
    p = sub.add_parser("network", help="DNS and basic connectivity diagnostics")
    p.add_argument("--host", default="example.com", help="Host you are allowed to query")
    p.add_argument("--json", dest="json_path")
    p = sub.add_parser("webcheck", help="Review HTTPS/TLS metadata and security headers")
    p.add_argument("url")
    p.add_argument("--json", dest="json_path")
    p = sub.add_parser("hash-create", help="Create a SHA-256 manifest for a folder")
    p.add_argument("directory")
    p.add_argument("--output", default="integrity.json")
    p = sub.add_parser("hash-verify", help="Verify a folder against a SHA-256 manifest")
    p.add_argument("directory")
    p.add_argument("--manifest", default="integrity.json")
    p = sub.add_parser("log-summary", help="Summarize patterns in a local log file")
    p.add_argument("logfile")
    p.add_argument("--json", dest="json_path")

    args = parser.parse_args()
    try:
        if args.command == "audit":
            emit(run_audit(), args.json_path)
        elif args.command == "network":
            emit(run_network_checks(args.host), args.json_path)
        elif args.command == "webcheck":
            emit(check_website(args.url), args.json_path)
        elif args.command == "hash-create":
            result = create_manifest(args.directory, args.output)
            emit(result)
        elif args.command == "hash-verify":
            emit(verify_manifest(args.directory, args.manifest))
        elif args.command == "log-summary":
            emit(summarize_log(args.logfile), args.json_path)
    except (OSError, ValueError) as exc:
        print(f"[!] Error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
