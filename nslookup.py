import dns.resolver

def fetch_nslookup_info(domain):
    record_types = ["A", "AAAA", "MX", "NS", "CNAME", "TXT"]
    results = {}

    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            results[record_type] = [answer.to_text() for answer in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            results[record_type] = ["No record found"]
        except dns.exception.DNSException as e:
            results[record_type] = [f"Error: {str(e)}"]

    return results


if __name__ == "__main__":    
    domain = "google.com"
    records = fetch_nslookup_info(domain)
    for record_type, values in records.items():
        print(f"{record_type} records:")
        for value in values:
            print(f"  - {value}")