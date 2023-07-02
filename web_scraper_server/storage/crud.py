from sqlalchemy.orm import Session

from settings import ITEMS_PER_PAGE
from . import models


def get_items(db: Session, skip: int = 0):
    return db.query(models.Apartment).offset(skip).limit(ITEMS_PER_PAGE).all()
