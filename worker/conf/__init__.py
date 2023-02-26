spider_name = "quote-spider"
spider_urls = ['https://quotes.toscrape.com']
QUOTE_SELECTOR = '.quote'
TEXT_SELECTOR = '.text::text'
AUTHOR_SELECTOR = '.author::text'
ABOUT_SELECTOR = '.author + a::attr("href")'
TAGS_SELECTOR = '.tags > .tag::text'
NEXT_SELECTOR = '.next a::attr("href")'