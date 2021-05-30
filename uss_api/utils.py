import re, base64


def is_valid_url(url:str, matcher=re.compile(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)")) -> bool:
    return matcher.match(url)

def urlhash(url:str) -> str:

    # return blake2s(url.encode(), digest_size=3).hexdigest()

    h = murmur32(bytes(url.encode()))
    return base64.b64encode(h.to_bytes(4, byteorder='little'), altchars=b'+-').decode()[:-2]


_MASK = (1 << 32) - 1
def murmur32_scramble(k:int) -> int:
    k *= 0xcc9e2d51
    k &= _MASK
    k = (k << 15) | (k >> 17)
    k &= _MASK
    k *= 0x1b873593
    return k & _MASK

def murmur32(key:bytes, seed=0x64786467) -> int:
    h = seed

    for i in range(len(key) >> 2):
        k = key[i]
        h ^= murmur32_scramble(k)
        h = (h << 13) | (h >> 19);
        h &= _MASK
        h = h * 5 + 0xe6546b64;
        h &= _MASK
        
    k = 0
    for i in range(len(key) & 2,0,-1):
        k <<= 8
        k |= key[i - 1]
        k &= _MASK
    
    h ^= murmur32_scramble(k)
    h ^= len(key)
    h ^= h >> 16
    h *= 0x85ebca6b
    h &= _MASK
    h ^= h >> 13
    h *= 0xc2b2ae35
    h &= _MASK
    h ^= h >> 16
    h &= _MASK
    return h