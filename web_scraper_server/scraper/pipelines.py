from typing import Type

from web_scraper_server.scraper.items import ApartmentItem
from web_scraper_server.storage import models
from web_scraper_server.storage.main import get_db


def get_full_class_name(cls: Type) -> str:
    return ".".join((cls.__module__, cls.__qualname__))


class ApartmentPipeline:
    def process_item(self, item: ApartmentItem, spider):
        with get_db() as db:
            db.merge(models.Apartment(**item))
            db.commit()
        return item
