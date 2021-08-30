import scrapy


class ProductItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    image_urls = scrapy.Field()
    all_sizes = scrapy.Field()
    all_colors = scrapy.Field()
    description = scrapy.Field()
    ratings = scrapy.Field()
    reviews = scrapy.Field()
