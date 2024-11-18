## detect malicious url — core engine by doneni
1. footprinting target domain (whois, nslookup, ssl cert, ...)
2. detect social engineering attacks
3. detect potential but dangerous risks

## dependencies
```
pip install python-whois
pip install dnspython
```

## run
1. create a `domain.txt` file at root directory
2. run `main.py`

```
python3 main.py
```

## project

```
├── dangerous_tld.py
├── detect_potential_risk.py
├── detect_social_engineering_attack.py
├── domain.txt
├── footprinting.py
├── idn_homograph.py
├── main.py
├── mutate_url
│   ├── mutate_url.py
│   ├── mutated_url.txt
│   └── target_url.txt
├── preprocessing.py
├── short_url.py
└── typo_squatting.py

```

### key modules
- `main.py` : run total inspection and detection
- `footprinting.py` : fetch whois, nslookup, ssl cert. output results as *JSON*
- `detect_social_engineering_attack.py` : detect social engineering attacks. output results as *JSON*
- `detect_potential_risk.py` : detect potential risks. output results as *JSON*

### extra files
- `dangerous_tld.py` : check if domain has dangerous tld
- `domain.txt` : a list of domains for dummy tests in `main.py`
- `idn_homograph.py` : detect mixed scripts
- `mutate_url`
  -  `mutate_url.py`: run mutator and craft typo-squatting greylist urls`
- `preprocessing.py` : extract root domain
- `short_url.py` : detect short_url and expand url
- `typo_squatting.py` : check if domain in `mutated_url.txt`