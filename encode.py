from os import urandom
from hashlib import sha256

'''Encode a URL using base62 encoding.'''
def base62_encode(url: str) -> str:
    # generate a unique hash for the URL
    hash = sha256(url.encode() + urandom(16)).hexdigest()
    hash2 = int(hash[:12], 16)

    # convert the hash to base62
    base62_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    base62 = ''
    while hash2:
        hash2, remainder = divmod(hash2, 62)
        base62 = base62_chars[remainder] + base62

    return base62
