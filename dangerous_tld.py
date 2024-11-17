import tldextract


dangerous_tlds = [
    "click",
    "win",
    "zip",
    "download",
    "party",
    "best",
    "top",
    "science",
    "account",
    "app",
    "xyz",
    "club",
    "work",
    "fun",
    "love",
    "company",
]


def is_dangerous_tld(domain):
    extracted = tldextract.extract(domain)
    return extracted.suffix in dangerous_tlds