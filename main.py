import footprinting

def test():
    df = open('./domain.txt', 'r')
    domain_list = df.read().split("\n")

    for domain in domain_list :
        print('URL: ' +domain)
        print(footprinting.dns_footprinting(domain))

if __name__ == "__main__":
    test()