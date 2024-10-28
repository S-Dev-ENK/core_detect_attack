import whois
import dns.resolver

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


def dns_footprinting(domain: str) -> dict:
    whois_info = fetch_whois_info(domain)
    nslookup_info = fetch_nslookup_info(domain)

    return {
        "whois": whois_info,
        "dns": nslookup_info
    }