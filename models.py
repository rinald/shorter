from datetime import datetime, timedelta
from sqlmodel import Field, SQLModel

class ShortUrl(SQLModel, table=True):
    hash: str = Field(primary_key=True)
    long_url: str = Field()
    created_date: str = Field(default_factory=lambda: datetime.now().isoformat())
    expiration_date: datetime = Field(default_factory=lambda: datetime.now() + timedelta(days=7))
