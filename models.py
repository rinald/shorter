from datetime import datetime, timedelta
from sqlmodel import Field, SQLModel


class ShortUrl(SQLModel, table=True):
    hash: str = Field(primary_key=True)
    long_url: str = Field()
    created_date: datetime = Field(default_factory=lambda: datetime.now())
    expiration_date: datetime = Field(default_factory=lambda: datetime.now() + timedelta(days=7))
    redirect_count: int = Field(default=0)

class Analytics(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    short_url: str = Field(foreign_key="shorturl.hash")

    timestamp: datetime = Field(default_factory=datetime.now)
    ip_address: str | None = Field(default=None)
    user_agent: str | None = Field(default=None)
