# Digits that are often used to imitate letters
LOOKALIKES = {
    "0": "o",
    "1": "l",
    "3": "e",
    "5": "s",
}


def find_lookalikes(domain):
    """Return a list of digits in the domain that look like letters."""
    found = []
    for character in domain:             # visit each character in turn
        if character in LOOKALIKES:      # is it a key in the dictionary?
            found.append(character)
    return found


def analyze_url(parts):
    """Take the dictionary from parse_url and return a list of warnings."""
    warnings = []                        # starts empty
    domain = parts["domain"]             # look up a value by its key

    if parts["scheme"] != "https":
        warnings.append({"message": "The link does not use HTTPS.", "points": 20})

    if domain.count("-") >= 2:
        warnings.append({"message": "The domain contains many hyphens.", "points": 15})

    if len(domain) > 30:
        warnings.append({"message": "The domain is unusually long.", "points": 10})

    lookalikes = find_lookalikes(domain)
    if len(lookalikes) > 0:
        warnings.append({"message": "The domain contains digits that look like letters.", "points": 30})

    return warnings


def calculate_score(warnings):
    """Add up the points from every warning."""
    total = 0
    for warning in warnings:
        total = total + warning["points"]
    return total


def risk_level(score):
    """Turn a numeric score into a label."""
    if score >= 50:
        return "High"
    elif score >= 20:
        return "Medium"
    else:
        return "Low"


if __name__ == "__main__":
    sample = {
        "scheme": "https",
        "domain": "paypa1-secure-login.com",
        "path": "/verify",
        "query": "",
    }
    found_warnings = analyze_url(sample)
    score = calculate_score(found_warnings)

    print(found_warnings)
    print(score)
    print(risk_level(score))