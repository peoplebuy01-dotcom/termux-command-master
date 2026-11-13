# Chapter 26 — Safe Network Diagnostics

अपने device के network की basic जाँच:
```bash
curl -I https://example.com
nslookup example.com
ip route
```

Connection failure को अलग-अलग समझें: internet connectivity, DNS resolution, TLS certificate और server response।

केवल अपने router या स्पष्ट अनुमति वाले network पर diagnostics करें। Port scanning, password guessing, exploitation या service disruption इस beginner guide का हिस्सा नहीं हैं।
