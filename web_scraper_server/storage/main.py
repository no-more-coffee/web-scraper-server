from contextlib import contextmanager

from web_scraper_server.storage.database import SessionLocal


# Dependency
@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
