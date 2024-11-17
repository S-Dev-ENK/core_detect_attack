import requests
import re
from urllib.parse import urlparse


SHORT_URL_DOMAINS = [
    "bit.ly", "t.co", "tinyurl.com", "goo.gl", "is.gd", 
    "buff.ly", "ow.ly", "rebrand.ly", "shorturl.at", 
    "s.id", "clck.ru"
]


def is_short_url(url):
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc

        if domain in SHORT_URL_DOMAINS:
            return True
        
        short_url_pattern = r"https?://[^/]{2,10}/\w{1,10}$"
        if re.match(short_url_pattern, url):
            return True
    
    except Exception as e:
        print("Error at is_short_url {e}")

    return False


def expand_url(short_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        res = requests.head(short_url, allow_redirects=True, headers=headers, timeout=5)

        if res.status_code in [301, 302]:
            print("Redirecting to {res.url}")
        return res.url
    
    except requests.exceptions.RequestException as e:
        print("Error at expand_url() {e}")


def test():
    df = open('./domain.txt', 'r')
    domain_list = df.read().split("\n")

    for domain in domain_list :
        if is_short_url(domain) is True:
            print(domain, "is shortened (" + expand_url(domain)+')')
        else:
            print(domain, "is not shortend")
        print()