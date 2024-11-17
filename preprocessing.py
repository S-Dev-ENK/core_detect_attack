from urllib.parse import urlparse

def preprocessing_domains(domain: str) -> str:
    parsed_url = urlparse(domain)
    domain_name = parsed_url.netloc or parsed_url.path
    
    if domain_name.startswith("www."):
        domain_name = domain_name[4:]
    
    if ':' in domain_name:
        domain_name = domain_name.split(':')[0]
    
    return domain_name

def test():
    domain = "http://asdf.asdf.sdaf.as-dsd.com"
    print(preprocessing_domains(domain))