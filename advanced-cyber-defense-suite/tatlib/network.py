"""Low-impact DNS and connectivity checks; deliberately no port scanning."""
import socket
import urllib.request


def run_network_checks(host):
    if not host or len(host) > 253 or any(ch.isspace() for ch in host):
        raise ValueError("Provide a valid hostname.")
    result = {"tool": "TAT Pro", "module": "network-diagnostics", "target": host,
              "scope": "DNS lookup and one HTTPS connectivity request only"}
    try:
        answers = sorted({item[4][0] for item in socket.getaddrinfo(host, None, type=socket.SOCK_STREAM)})
        result["dns"] = {"status": "OK", "addresses": answers}
    except socket.gaierror as exc:
        result["dns"] = {"status": "ERROR", "detail": str(exc)}
    try:
        req = urllib.request.Request("https://" + host.rstrip("/"), method="HEAD",
                                     headers={"User-Agent": "TAT-Pro-Defensive-Toolkit/1.0"})
        with urllib.request.urlopen(req, timeout=5) as response:
            result["https"] = {"status": "OK", "http_status": response.status}
    except Exception as exc:
        result["https"] = {"status": "REVIEW", "detail": str(exc)}
    return result
