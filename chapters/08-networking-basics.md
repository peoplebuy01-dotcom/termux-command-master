# Chapter 08 — Networking Fundamentals

## Concepts
- IP address: network पर device का address
- DNS: domain name को IP में resolve करता है
- Port: किसी service का logical endpoint
- HTTP/HTTPS: web communication protocols

## Safe diagnostic commands
```bash
pkg install curl dnsutils
curl -I https://example.com
nslookup example.com
```

## अपना local network समझें
```bash
ip addr
ip route
```
कुछ Android/Termux builds में `ip` command अलग package से मिल सकती है या सीमित हो सकती है।

## Safety
केवल अपने network या स्पष्ट अनुमति वाले systems की जाँच करें। दूसरों के Wi-Fi, accounts या servers में घुसने, password guessing या disruption की कोशिश न करें।

## अभ्यास
किसी सार्वजनिक वेबसाइट का HTTPS response header `curl -I` से देखें और status code का अर्थ समझें।
