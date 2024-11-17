import short_url
import dangerous_tld
import json


def detect_potential_risk(domain):
    is_short_url = short_url.is_short_url(domain)
    is_dangerous_tld = dangerous_tld.is_dangerous_tld(domain)

    potential_risk_detected = is_short_url or is_dangerous_tld

    result = {
        "has_potential_risk" : potential_risk_detected,
        "short_url_attack": is_short_url,
        "dangerous_tld_attack": is_dangerous_tld,
    }

    return json.dumps(result, indent=4)


def test() :
    domain = "hey.zip"
    print(detect_potential_risk(domain))