from web_scraper_server.scraper.pipelines import ApartmentPipeline, get_full_class_name

SPIDER_MODULES = ["web_scraper_server.scraper.spiders"]
NEWSPIDER_MODULE = "web_scraper_server.scraper.spiders"

ITEM_PIPELINES = {
    get_full_class_name(ApartmentPipeline): 1000,
}
