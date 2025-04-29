from fastapi import Request

from database import SessionDep
from models import ShortUrl, Analytics

def create_analytics_record(url: ShortUrl, session: SessionDep, request: Request):
    # update existing short url record (increment redirect_count)
    url.redirect_count += 1
    session.commit()

    # create a new analytics record
    record = Analytics(
        short_url=url.hash,
        ip_address=request.client.host if request.client is not None else None,
        user_agent=request.headers.get("User-Agent"),
    )

    session.add(record)
    session.commit()
