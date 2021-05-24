import redis
from dal import get_url_by_key, add_url_key
from model import Url

rc = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

async def get(ctx, key:str) -> Url:
    res = Url()
    res.url = rc.get(key)
    if res.url:
        return res

    res = await get_url_by_key(ctx, key)
    return res

async def set(ctx, key:str, url:str) -> Url:
    res = Url()
    res.url = rc.get(key)
    res.hash = key

    if res.url == url:
        return res
    res = await add_url_key(ctx, url, key)
    rc.set(key, url)

    return res