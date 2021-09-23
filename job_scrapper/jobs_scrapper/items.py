import scrapy


class JobItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    website_name = scrapy.Field()
    age = scrapy.Field()
