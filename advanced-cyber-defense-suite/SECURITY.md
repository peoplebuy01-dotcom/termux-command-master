# Security Policy

## Intended use
TAT Pro is a defensive learning and system-administration toolkit. Run it only on devices, files, networks, and websites you own or are explicitly authorized to assess.

## Reporting a vulnerability
Do not publish secrets, tokens, personal logs, or exploitable details in a public issue. Contact the repository maintainer privately through the contact method listed on the GitHub profile.

## Safe defaults
- No exploit modules, credential attacks, stealth, persistence, or malware.
- Network module performs DNS and basic connectivity checks only.
- File integrity commands read files and write a manifest; they do not modify source files.
- Web checks make a normal HTTP(S) request to the URL explicitly supplied by the operator.
