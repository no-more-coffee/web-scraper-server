from typing import Dict, Iterator

import fnc
import scrapy

from web_scraper_server.scraper.items import ApartmentItem


class ApartmentSpider(scrapy.Spider):
    name = "apartments"
    start_urls = [
        f"https://www.sreality.cz/api/en/v2/estates?category_main_cb=1&category_type_cb=1&page={page}&per_page=10"
        for page in range(1, 2)
    ]

    def parse(self, response, **kwargs) -> Iterator[Dict[str, str]]:
        yield from parse_data(response.json())


def parse_data(data: dict) -> Iterator[Dict[str, str]]:
    yield from fnc.compose(
        (fnc.get, "_embedded.estates"),
        (fnc.map, ("hash_id", "locality", "_links.images[0].href")),
        (fnc.map, lambda item: ApartmentItem(id=item[0], title=item[1], image=item[2])),
    )(data)
