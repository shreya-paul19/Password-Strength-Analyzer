import re

def analyze_password(password):

    score = 0

    if len(password) >= 12:
        score += 25

    if re.search(r'[A-Z]', password):
        score += 15

    if re.search(r'[a-z]', password):
        score += 15

    if re.search(r'[0-9]', password):
        score += 15

    if re.search(r'[^A-Za-z0-9]', password):
        score += 15

    if len(password) > 0 and len(set(password)) == len(password):
        score += 15

    common = False

    try:
        with open("common_passwords.txt", "r") as file:
            common_passwords = [line.strip() for line in file]

        if password.lower() in common_passwords:
            common = True
            score = max(score - 30, 0)

    except:
        pass

    if score < 40:
        strength = "Weak"
    elif score < 70:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "score": score,
        "strength": strength,
        "common": common
    }