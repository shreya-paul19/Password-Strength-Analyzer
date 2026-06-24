import re

def check_policy(password):

    return {
        "length": len(password) >= 12,
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "number": bool(re.search(r'[0-9]', password)),
        "special": bool(re.search(r'[^A-Za-z0-9]', password))
    }