# Chapter 18 — APIs और curl

API software के बीच data exchange का तरीका है। HTTP status code response की स्थिति बताता है।

```bash
pkg install curl
curl -I https://example.com
curl -L https://example.com
```

- 2xx: सामान्यतः success
- 3xx: redirect
- 4xx: request/client समस्या
- 5xx: server समस्या

JSON response पढ़ने के लिए optional `jq`:
```bash
pkg install jq
curl -s https://api.github.com | jq '.current_user_url'
```

Public APIs की rate limits और terms मानें। API key को command history या public repository में न रखें।
