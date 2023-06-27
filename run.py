from scrapy.cmdline import execute
import scrapy.__main__


def main():
    execute(argv=[scrapy.__main__.__file__, "runspider", "web_scraper_server/spiders.py"])


if __name__ == '__main__':
    main()
