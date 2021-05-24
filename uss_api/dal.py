from model import Url
from sqlalchemy.orm import Session
from sqlalchemy import select

async def get_url_by_key(ctx, key) -> Url:
    session: Session = ctx.session
    async with session.begin():
        stmt = select(Url).where(Url.hash == key)
        result = await session.execute(stmt)
        url:Url = result.scalar()
    return url

async def add_url_key(ctx, url, key) -> Url:
    session: Session = ctx.session
    async with session.begin():
        stmt = select(Url).where(Url.hash == key)
        res = await session.execute(stmt)
        res:Url = res.scalar()

        if res:
            res.url = url
        else:
            res = Url(url=url, hash=key)
        await session.merge(res)
    
    return res