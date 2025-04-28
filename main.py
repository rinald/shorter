from typing import Annotated
from datetime import datetime, timedelta
from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from sqlmodel import Field, Session, SQLModel, create_engine, select

from encode import base62_encode

class ShortUrl(SQLModel, table=True):
    hash: str = Field(primary_key=True)
    long_url: str = Field()
    created_date: str = Field(default_factory=lambda: datetime.now().isoformat())
    expiration_date: datetime = Field(default_factory=lambda: datetime.now() + timedelta(days=7))

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

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
