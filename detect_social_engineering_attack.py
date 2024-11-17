import json
import idn_homograph
import typo_squatting


def detect_social_engineer_attack(domain):
    typosquatting_result = typo_squatting.check_typosquatting(domain)
    mixed_scripts_result = idn_homograph.check_idn_homograph_attack(domain)
    
    attack_detected = False

    if typosquatting_result or mixed_scripts_result:
        attack_detected = True

    result = {
        "attack_detected": attack_detected,
        "typosquatting_attack": typosquatting_result,
        "mixed_scripts_attack": mixed_scripts_result,
    }

    return json.dumps(result, indent=4)


def test():
    domain = "https://example.com/Ρho"
    print(detect_social_engineer_attack(domain))