from scrapy import Spider, Request
from conf import spider_name, spider_urls


class QuoteSpider(Spider):
    name = spider_name
    start_urls = spider_urls

    def parse(self, response, **kwargs):
        count = 0
        QUOTE_SELECTOR = '.quote'
        TEXT_SELECTOR = '.text::text'
        AUTHOR_SELECTOR = '.author::text'
        ABOUT_SELECTOR = '.author + a::attr("href")'
        TAGS_SELECTOR = '.tags > .tag::text'
        NEXT_SELECTOR = '.next a::attr("href")'

        for quote in response.css(QUOTE_SELECTOR):
            count += 1
            yield {
                'text': quote.css(TEXT_SELECTOR).extract_first(),
                'author': quote.css(AUTHOR_SELECTOR).extract_first(),
                'about': 'https://quotes.toscrape.com' + quote.css(ABOUT_SELECTOR).extract_first(),
                'tags': quote.css(TAGS_SELECTOR).extract(),
            }
        next_page = response.css(NEXT_SELECTOR).extract_first()
        if next_page:
            yield Request(response.urljoin(next_page))