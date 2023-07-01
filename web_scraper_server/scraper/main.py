from scrapy.crawler import CrawlerProcess

from web_scraper_server.scraper.pipelines import ApartmentPipeline, get_full_class_name
from web_scraper_server.scraper.spiders import ApartmentSpider


def run_crawler():
    process = CrawlerProcess(
        settings={
            "ITEM_PIPELINES": {
                get_full_class_name(ApartmentPipeline): 1000,
            },
        },
    )
    process.crawl(ApartmentSpider)
    process.start()  # the script will block here until the crawling is finished


if __name__ == "__main__":
    run_crawler()
