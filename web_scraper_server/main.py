import httpx
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from web_scraper_server.storage import crud, models, schemas
from web_scraper_server.storage.database import engine
from web_scraper_server.storage.main import get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="web_scraper_server/static"), name="static")
templates = Jinja2Templates(directory="web_scraper_server/templates")


@app.get("/apartments", response_model=list[schemas.Apartment])
async def read_items(
    skip: int = 0, limit: int = 100, db_context: Session = Depends(get_db)
):
    with db_context as db:
        return crud.get_items(db, skip=skip, limit=limit)


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    url = str(request.url_for("read_items"))
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    items = response.json()
    return templates.TemplateResponse(
        "index.html", {"request": request, "page": 1, "items": items}
    )
