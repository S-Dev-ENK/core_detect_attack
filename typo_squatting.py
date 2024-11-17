def check_typosquatting(domain):
    mutated_file = './mutate_url/mutated_url.txt'

    with open(mutated_file, 'r') as file:
        mutated_urls = [line.strip() for line in file.readlines()]

    return domain in mutated_urls


def test():
    domain = "naevr.com"
    print(check_typosquatting(domain))