# web-scraper-server

Simple web scraper server.

Fulfills requirements:

- Use [scrapy](https://docs.scrapy.org) framework to scrape the first 500 items (title, image url)
    - from [sreality.cz](https://www.sreality.cz) (flats, sell)
- Save it in the Postgresql database.
- Implement a simple HTTP server in python and show these 500 items on a simple page (title and image)
- Put everything to single docker-compose command so that I can just run "docker-compose up" in the Github repository
    - and see the scraped ads on http://127.0.0.1:8080 page.

## Requirements

- Docker

## Usage

- Run docker services

```shell
docker compose up
```

- Wait 10 seconds (default) for scraper to be able to collect the data
- Head to [Home page](http://127.0.0.1:8080)

## Development

### Creating local environment

```shell
cp envs/local.env.skeleton envs/local.env
```
