import whois
import dns.resolver
import ssl
import socket
import json
from datetime import datetime

def fetch_whois_info(domain: str) -> dict:
    try:
        whois_info = whois.whois(domain)
        return dict(whois_info)
    except Exception as e:
        print(f"WHOIS search error: {e}")
        return {}


def fetch_nslookup_info(domain: str) -> dict:
    dns_info = {"A": [], "MX": [], "TXT": []}
    try:
        a_records = dns.resolver.resolve(domain, 'A')
        dns_info["A"] = [record.to_text() for record in a_records]
    except dns.resolver.NoAnswer:
        dns_info["A"] = None
    except Exception as e:
        print(f"Nslookup A record search error: {e}")
    
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        dns_info["MX"] = [record.to_text() for record in mx_records]
    except dns.resolver.NoAnswer:
        dns_info["MX"] = None
    except Exception as e:
        print(f"Nslookup MX record search error: {e}")
    
    try:
        txt_records = dns.resolver.resolve(domain, 'TXT')
        dns_info["TXT"] = [record.to_text() for record in txt_records]
    except dns.resolver.NoAnswer:
        dns_info["TXT"] = None
    except Exception as e:
        print(f"Nslookup TXT record search error: {e}")

    return dns_info


def fetch_ssl_certificate_info(domain: str) -> dict:
    cert_info = {}
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                cert_info = {
                    "subject": dict(x[0] for x in cert.get("subject", [])),
                    "issuer": dict(x[0] for x in cert.get("issuer", [])),
                    "version": cert.get("version"),
                    "serialNumber": cert.get("serialNumber"),
                    "notBefore": cert.get("notBefore"),
                    "notAfter": cert.get("notAfter"),
                    "subjectAltName": cert.get("subjectAltName")
                }
                if isinstance(cert_info.get("notBefore"), datetime):
                    cert_info["notBefore"] = cert_info["notBefore"].strftime('%Y-%m-%d %H:%M:%S')
                if isinstance(cert_info.get("notAfter"), datetime):
                    cert_info["notAfter"] = cert_info["notAfter"].strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        print(f"SSL certificate fetch error: {e}")
    return cert_info


def datetime_converter(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    raise TypeError("Type not serializable")

def dns_footprinting(domain: str) -> str:
    whois_info = fetch_whois_info(domain)
    nslookup_info = fetch_nslookup_info(domain)
    ssl_certificate_info = fetch_ssl_certificate_info(domain)

    footprint_data = {
        "whois": whois_info,
        "dns": nslookup_info,
        "cert": ssl_certificate_info
    }

    footprint_json = json.dumps(footprint_data, indent=4, default=datetime_converter)
    return footprint_json


def test():
    domain = "google.com"
    footprint_json = dns_footprinting(domain)
    print(footprint_json)