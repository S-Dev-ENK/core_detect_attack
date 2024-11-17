import re

def get_root_url(url):
    url = re.sub(r'^(https?://|www\.)', '', url)
    return url


def contains_latin(url):
    latin_pattern = re.compile(r'[A-Za-z]')

    if latin_pattern.search(url):
        return True
    return False


def contains_cyrillic(url):
    cyrillic_pattern = re.compile(r'[\u0400-\u04FF]')
    
    if cyrillic_pattern.search(url):
        return True
    return False


def contains_greek(url):
    greek_pattern = re.compile(r'[\u0370-\u03FF]')

    if greek_pattern.search(url):
        return True
    return False


def contains_armenian(url):
    armenian_pattern = re.compile(r'[\u0530-\u058F]')

    if armenian_pattern.search(url):
        return True
    return False


def get_used_scripts(url):
    url = get_root_url(url)
    used_scripts = []
    if(contains_latin(url)):
        used_scripts.append('latin')
    if(contains_cyrillic(url)):
        used_scripts.append('cyrillic')
    if(contains_armenian(url)):
        used_scripts.append('armenian')
    if(contains_greek(url)):
        used_scripts.append('greek')
    
    return used_scripts


def check_idn_homograph_attack(url):
    used_scripts = get_used_scripts(url)

    return len(used_scripts) > 1


def test():
    df = open('./domain.txt', 'r')
    domain_list = df.read().split("\n")

    for domain in domain_list :
        print("url: ", domain)
        print('used_scripts:', get_used_scripts(domain))
        print('mixed_scripts:', check_idn_homograph_attack(domain))
        print()