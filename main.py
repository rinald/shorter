from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from sqlmodel import select

from encode import base62_encode
from models import ShortUrl
from database import SessionDep, create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# shorten url
@app.post("/shorten")
async def shorten_url(body: ShortUrl, session: SessionDep):
    hash = base62_encode(body.long_url)
    body.hash = hash

    session.add(body)
    session.commit()
    session.refresh(body)
    return body

# get url
@app.get("/url/{hash}")
async def get_url(hash: str, session: SessionDep):
    statement = select(ShortUrl).where(ShortUrl.hash == hash)
    url = session.exec(statement).first()
    if url:
        return RedirectResponse(url.long_url, status_code=301)
    else:
        return {"error": "URL not found"}
