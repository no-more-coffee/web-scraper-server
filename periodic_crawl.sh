set -o nounset  # Do no allow unset variables

while true
do
    echo Wait $TIMEOUT_SECONDS seconds
    sleep $TIMEOUT_SECONDS

    scrapy crawl apartments
done
