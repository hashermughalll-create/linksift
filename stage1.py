from urllib.parse import urlparse


def parse_url(raw_url):
    """Clean a URL string and return its parts as a dictionary."""
    raw_url = raw_url.strip()          # remove spaces around the text

    if raw_url == "":
        raise ValueError("The URL is empty.")

    if len(raw_url) > 200:
        raise ValueError("The URL is too long (over 200 characters).")

    if "://" not in raw_url:           # no scheme given, so add one
        raw_url = "https://" + raw_url

    parts = urlparse(raw_url)

    if parts.hostname is None:
        raise ValueError("No domain found in the URL.")

    if ".." in parts.hostname:
        raise ValueError("The domain contains consecutive dots.")

    return {
        "scheme": parts.scheme,
        "domain": parts.hostname,
        "path": parts.path,
        "query": parts.query,
    }


if __name__ == "__main__":
    try:
        result = parse_url("  paypa1-secure.com/login  ")
        print(result)
    except ValueError as error:
        print("Problem:", error)