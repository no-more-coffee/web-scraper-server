from typing import Dict, Iterator

import fnc
import scrapy

from settings import MAX_SCRAPE_ITEMS, ITEMS_PER_PAGE
from web_scraper_server.scraper.items import ApartmentItem

URL_BASE = "https://www.sreality.cz/api/en/v2/estates"


class ApartmentSpider(scrapy.Spider):
    name = "apartments"
    iterations_count = MAX_SCRAPE_ITEMS // ITEMS_PER_PAGE
    start_urls = [
        f"{URL_BASE}?category_main_cb=1&category_type_cb=1&page={page}&per_page={ITEMS_PER_PAGE}"
        for page in range(1, iterations_count + 1)
    ]

    def parse(self, response, **kwargs) -> Iterator[Dict[str, str]]:
        yield from parse_data(response.json())


def parse_data(data: dict) -> Iterator[Dict[str, str]]:
    yield from fnc.compose(
        (fnc.get, "_embedded.estates"),
        (fnc.map, ("hash_id", "locality", "_links.images[0].href")),
        (fnc.map, lambda item: ApartmentItem(id=item[0], title=item[1], image=item[2])),
    )(data)
