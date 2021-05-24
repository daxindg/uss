import re
from hashlib import blake2s


def is_valid_url(url:str, matcher=re.compile(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)")):
    return matcher.match(url)

def urlhash(url:str):
    return blake2s(url.encode(), digest_size=3).hexdigest()
