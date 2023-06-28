from typing import Dict, Iterator

import fnc
import scrapy


class ApartmentsSpider(scrapy.Spider):
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
        (fnc.map, ("locality", "_links.images[0].href")),
        (fnc.map, lambda x: {"title": x[0], "image": x[1]}),
    )(data)
