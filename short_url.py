import requests
import re
from urllib.parse import urlparse


SHORT_URL_DOMAINS = [
    "bit.ly", "t.co", "tinyurl.com", "goo.gl", "is.gd", 
    "buff.ly", "ow.ly", "rebrand.ly", "shorturl.at", 
    "s.id", "clck.ru", "vo.la",
]


def normalize_url(url):
    if not re.match(r'https?://', url):
        url = 'http://' + url
    return url


def is_short_url(url):
    try:
        url = normalize_url(url)
        parsed_url = urlparse(url)
        domain = parsed_url.netloc

        if domain in SHORT_URL_DOMAINS:
            return True
        
        short_url_pattern = r"https?://[^/]{2,10}/\w{1,10}$"
        if re.match(short_url_pattern, url):
            return True
    
    except Exception as e:
        print(f"Error at is_short_url: {e}")

    return False


def expand_url(short_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        res = requests.head(short_url, allow_redirects=True, headers=headers, timeout=5)

        if res.status_code in [301, 302]:
            print(f"Redirecting to {res.url}")
        return res.url
    
    except requests.exceptions.RequestException as e:
        print(f"Error at expand_url: {e}")


def test():
    with open('./domain.txt', 'r') as df:
        domain_list = df.read().splitlines()

    for domain in domain_list:
        domain_url = normalize_url(domain)
        if is_short_url(domain_url):
            expanded_url = expand_url(domain_url)
            print(f"{domain} is shortened ({expanded_url})")
        else:
            print(f"{domain} is not shortened")
        print()