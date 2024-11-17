import sys
import os
import requests
import dnstwist

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import preprocessing

def read_target_urls(filename):
    with open(filename, 'r') as file:
        return [preprocessing.preprocessing_domains(line.strip()) for line in file.readlines()]


def check_url_exists(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False


def generate_similar_domains(domain):
    dt = dnstwist.run(domain=domain, registered=True, format='null')
    return [entry['domain'] for entry in dt]


def write_to_file(filename, urls):
    with open(filename, 'a') as file:
        for url in urls:
            file.write(url + '\n')


def mutate_url():
    target_file = 'mutate_url/target_url.txt'
    output_file = 'mutate_url/mutated_url.txt'

    target_urls = read_target_urls(target_file)

    for domain in target_urls:
        print(f"[*] Generating typosquatting domains for: {domain}")
        similar_domains = generate_similar_domains(domain)

        for similar_domain in similar_domains:
            url = f"{similar_domain}"
            if check_url_exists(url):
                print(f"[+] Found existing domain: {url}")
                write_to_file(output_file, [url])
            else:
                print(f"[-] Domain does not exist: {url}")


if __name__ == "__main__":
    mutate_url()
