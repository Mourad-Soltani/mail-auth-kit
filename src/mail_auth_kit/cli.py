"""
CLI for mail-auth-kit
Signature: Mourad.Soltani
"""

import argparse
import sys

def generate_spf(domain: str) -> str:
    return f"v=spf1 include:_spf.google.com include:sendgrid.net ~all  # for {domain}"

def generate_dkim(selector: str, domain: str) -> str:
    return f"{selector}._domainkey.{domain} IN TXT \"v=DKIM1; k=rsa; p=YOUR_PUBLIC_KEY_HERE\""

def generate_dmarc(domain: str) -> str:
    return f"_dmarc.{domain} IN TXT \"v=DMARC1; p=none; rua=mailto:dmarc@{domain}\""

def main():
    parser = argparse.ArgumentParser(description="Generate SPF, DKIM, DMARC records for solo founders")
    parser.add_argument("--domain", required=True, help="Your domain")
    parser.add_argument("--selector", default="default", help="DKIM selector")
    args = parser.parse_args()

    print("=== SPF Record ===")
    print(generate_spf(args.domain))
    print("\n=== DKIM Guidance ===")
    print(generate_dkim(args.selector, args.domain))
    print("\n=== DMARC Record ===")
    print(generate_dmarc(args.domain))
    print("\nTip: Start with p=none for monitoring. Signature: Mourad.Soltani")

if __name__ == "__main__":
    main()
