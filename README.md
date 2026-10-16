# mail-auth-kit

A minimal CLI tool for solo founders and freelancers to generate SPF, DKIM, and DMARC DNS records for better email deliverability.

**Signature: Mourad.Soltani**

## Features
- Generate recommended SPF record
- Generate basic DKIM setup guidance
- Generate DMARC policy record
- Simple explanations for each

## Installation
```bash
pip install -e .
```

## Usage
```bash
python -m mail_auth_kit --domain example.com --selector default
```

## Health Tests
Run `pytest` to verify the tool is healthy.

## License
MIT - see LICENSE

---
Built by Mourad.Soltani
