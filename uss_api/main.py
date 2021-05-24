from sanic import Sanic
from sanic.response import json, redirect
from utils import is_valid_url, urlhash
from contextvars import ContextVar
from cache import get, set
from sanic_cors import CORS, cross_origin

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

app = Sanic('app')
CORS(app)

bind = create_async_engine("mysql+aiomysql://xxdg:simplepassword@localhost:3306/ussapi", echo=True)

_base_model_session_ctx = ContextVar("session")

@app.middleware("request")
async def inject_session(request):
    request.ctx.session = sessionmaker(bind, AsyncSession, expire_on_commit=False)()
    request.ctx.session_ctx_token = _base_model_session_ctx.set(request.ctx.session)

@app.middleware("response")
async def close_session(request, response):
    if hasattr(request.ctx, "session_ctx_token"):
        _base_model_session_ctx.reset(request.ctx.session_ctx_token)
        await request.ctx.session.close()

@app.get("/<key:[a-zA-Z0-9]+>")
async def main(request, key: str):
    url = await get(request.ctx, key)
    if not url:
        return redirect('/') 

    return redirect(url.url)

@app.post("/create")
async def create(request):
    url:str = request.form.get("url").strip()
    
    if url is None or not is_valid_url(url):
        return json({
                "ok": False,
                "err": "bad url"
            })

    ufurl = url.replace("https://", "").replace("http://", "")
    key = urlhash(ufurl)

    res = await set(request.ctx, key, url)
    return json({"ok":True, "data": res.to_dict()})