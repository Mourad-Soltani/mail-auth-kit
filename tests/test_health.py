"""
Health tests for mail-auth-kit
Signature: Mourad.Soltani
"""

import pytest
from mail_auth_kit.cli import generate_spf, generate_dkim, generate_dmarc

def test_spf_generation():
    result = generate_spf("example.com")
    assert "v=spf1" in result
    assert "example.com" in result

def test_dkim_generation():
    result = generate_dkim("s1", "example.com")
    assert "s1._domainkey.example.com" in result
    assert "v=DKIM1" in result

def test_dmarc_generation():
    result = generate_dmarc("example.com")
    assert "_dmarc.example.com" in result
    assert "v=DMARC1" in result
    assert "p=none" in result

def test_health():
    assert True  # Basic health check
