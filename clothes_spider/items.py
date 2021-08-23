import scrapy

class ImageItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    image_urls = scrapy.Field()
    files = scrapy.Field()
