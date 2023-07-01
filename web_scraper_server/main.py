from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from web_scraper_server.storage import crud, models, schemas
from web_scraper_server.storage.database import engine
from web_scraper_server.storage.main import get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/", response_model=list[schemas.Apartment])
def read_items(skip: int = 0, limit: int = 100, db_context: Session = Depends(get_db)):
    with db_context as db:
        return crud.get_items(db, skip=skip, limit=limit)
