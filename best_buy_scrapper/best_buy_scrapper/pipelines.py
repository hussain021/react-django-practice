# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class BestBuyScrapperPipeline:
    def process_item(self, item, spider):
        for key in item.keys():
            if key is None:
                raise DropItem("No {} Found".format(key))
            else:
                return item
