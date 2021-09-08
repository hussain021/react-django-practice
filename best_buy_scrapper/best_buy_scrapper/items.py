# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class ProductItem(scrapy.Item):
    language = scrapy.Field()
    category = scrapy.Field()
    brand = scrapy.Field()
    url = scrapy.Field()
    scraped_date = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    specification = scrapy.Field()
    image_urls = scrapy.Field()
    skus = scrapy.Field()
