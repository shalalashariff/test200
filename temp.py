print("sggdujf")

import scrapy


class QuoteSPider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        texts = response.css('span.text::text').extract()
        authors = response.css('small.author::text').extract()
        links = response.xpath('//div[@class="quote]/span/a/@href').extract()
        tags = response.css('meta.keywords').xpath('@content').getall()
        domain = 'quotes.toscrape.com'
        items = zip(texts, authors, tags, links)
        for i in items:
            dict_quotes = {'Quotes': i[0],
                           'Authors': i[1],
                           'Tags': i[2],
                           'Link to author': domain + i[3]}
            yield dict_quotes
