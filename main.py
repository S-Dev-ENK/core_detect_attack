import preprocessing
import footprinting
import detect_social_engineering_attack
import detect_potential_risk


if __name__ == "__main__":
    df = open('./domain.txt', 'r') # dummy
    domain_list = df.read().split("\n")

    for domain in domain_list:
        if not domain.strip():
            continue

        domain = preprocessing.preprocessing_domain(domain)

        footprinting_json = footprinting.dns_footprinting(domain)
        social_engineering_attack_json = detect_social_engineering_attack.detect_social_engineer_attack(domain)
        potential_risk_json = detect_potential_risk.detect_potential_risk(domain)
        
        print(domain)
        print(footprinting_json)
        print(social_engineering_attack_json)
        print(potential_risk_json)
        print()