from urllib.parse import urlparse

url = "https://login.paypa1-secure.com/verify/account?id=123"

parts = urlparse(url)

print(parts.scheme)
print(parts.netloc)
print(parts.path)
print(parts.query)