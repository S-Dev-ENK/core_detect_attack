import short_url
import dangerous_tld
import json


def detect_potential_risk(domain):
    short_url_attack = short_url.is_short_url(domain)
    dangerous_tld_attack = dangerous_tld.is_dangerous_tld(domain)

    attack_detected = short_url_attack or dangerous_tld_attack

    result = {
        "has_potential_risk" : attack_detected,
        "short_url_attack": short_url_attack,
        "dangerous_tld_attack": dangerous_tld_attack,
    }

    return json.dumps(result, indent=4)


def test() :
    domain = "hey.zip"
    print(detect_potential_risk(domain))