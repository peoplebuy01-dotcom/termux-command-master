"""Basic security-header and TLS certificate metadata review for authorized URLs."""
import ssl
import urllib.error
import urllib.parse
import urllib.request


SECURITY_HEADERS = {
    "strict-transport-security": "Encourages HTTPS on future visits",
    "content-security-policy": "Helps restrict content sources",
    "x-content-type-options": "Helps prevent MIME-type sniffing",
    "referrer-policy": "Controls referrer information",
    "permissions-policy": "Restricts selected browser features",
}


def check_website(url):
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname:
        raise ValueError("Use a complete HTTPS URL, for example https://example.com")
    if parsed.username or parsed.password:
        raise ValueError("URLs containing embedded credentials are not accepted.")
    req = urllib.request.Request(url, headers={"User-Agent": "TAT-Pro-Defensive-Toolkit/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=8) as response:
            headers = {k.lower(): v for k, v in response.headers.items()}
            status = response.status
            final_url = response.geturl()
    except urllib.error.HTTPError as exc:
        headers = {k.lower(): v for k, v in exc.headers.items()}
        status, final_url = exc.code, exc.geturl()
    except Exception as exc:
        raise ValueError(f"HTTPS request failed: {exc}") from exc

    missing = [name for name in SECURITY_HEADERS if name not in headers]
    tls = {"note": "Certificate chain was validated by Python's default TLS context during the HTTPS request."}
    return {"tool": "TAT Pro", "module": "web-security-review", "url": url,
            "final_url": final_url, "http_status": status, "tls": tls,
            "headers": {name: {"present": name in headers, "purpose": purpose,
                               "value": headers.get(name)} for name, purpose in SECURITY_HEADERS.items()},
            "review_items": [f"Missing header: {name}" for name in missing],
            "note": "Header presence alone does not prove a site is secure. Review values and application behavior."}
