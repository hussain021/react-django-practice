import scrapy

from clothes_spider.items import ImageItem


class SheegoSpider(scrapy.Spider):
    name = 'sheego_scrapping'
    allowed_domains = ['sheego.de']
    start_urls = ['https://www.sheego.de/neu/neue-blusen-tuniken', 'https://www.sheego.de/neu/neue-hosen',
    'https://www.sheego.de/neu/neue-kleider', 'https://www.sheego.de/neu/neue-shirts-tops',
    'https://www.sheego.de/neu/trendstyles', 'https://www.sheego.de/neu/kundenlieblinge',
    'https://www.sheego.de/damenmode/abendmode', 'https://www.sheego.de/damenmode/accessoires',
    'https://www.sheego.de/damenmode/bademode', 'https://www.sheego.de/damenmode/basic-mode',
    'https://www.sheego.de/damenmode/businessmode', 'https://www.sheego.de/damenmode/joe-browns',
    'https://www.sheego.de/damenmode/schuhe', 'https://www.sheego.de/damenmode/sportbekleidung',
    'https://www.sheego.de/damenmode/?filterNeuware=true', 'https://www.sheego.de/damenmode/blusen-tuniken',
    'https://www.sheego.de/damenmode/dirndl-trachten', 'https://www.sheego.de/damenmode/hosen',
    'https://www.sheego.de/damenmode/jacken-maentel', 'https://www.sheego.de/damenmode/jeans',
    'https://www.sheego.de/damenmode/kleider', 'https://www.sheego.de/damenmode/pullover-strickjacken',
    'https://www.sheego.de/damenmode/roecke', 'https://www.sheego.de/damenmode/shirts-tops',
    'https://www.sheego.de/damenmode/sweatshirts-sweatjacken', 'https://www.sheego.de/damenmode/jeans/jeansjacken',
    'https://www.sheego.de/damenmode/jeans/jeanskleider', 'https://www.sheego.de/damenmode/jeans/jeansroecke',
    'https://www.sheego.de/damenmode/jeans/jeggings', 'https://www.sheego.de/damenmode/jeans/jeansbluse',
    'https://www.sheego.de/damenmode/jeans/jeans-tunika',
    'https://www.sheego.de/damenmode/jeans/jeanshosen/bootcut-jeans',
    'https://www.sheego.de/damenmode/jeans/jeanshosen', 'https://www.sheego.de/damenmode/jeans/jeanshosen/caprijeans',
    'https://www.sheego.de/damenmode/jeans/jeanshosen/jeans-bermudas',
    'https://www.sheego.de/damenmode/jeans/jeanshosen/destroyed-jeans',
    'https://www.sheego.de/damenmode/jeans/jeanshosen/skinny-jeans',
    'https://www.sheego.de/damenmode/jeans/jeanshosen/slim-fit-jeans',
    'https://www.sheego.de/damenmode/jeans/jeanshosen/stretch-jeans',
    'https://www.sheego.de/damenmode/jeans/jeanshosen/straight-jeans',
    'https://www.sheego.de/damenmode/jeans/jeanshosen/7-8-jeans',
    'https://www.sheego.de/damenmode/kleider/abendkleider', 'https://www.sheego.de/damenmode/kleider/businesskleider',
    'https://www.sheego.de/damenmode/kleider/freizeitkleider', 'https://www.sheego.de/damenmode/kleider/partykleider',
    'https://www.sheego.de/damenmode/kleider/sommerkleider', 'https://www.sheego.de/damenmode/kleider/cocktailkleider',
    'https://www.sheego.de/damenmode/kleider/dirndlkleider', 'https://www.sheego.de/damenmode/kleider/etuikleider',
    'https://www.sheego.de/damenmode/kleider/jeanskleider', 'https://www.sheego.de/damenmode/kleider/jerseykleider',
    'https://www.sheego.de/damenmode/kleider/maxikleider', 'https://www.sheego.de/damenmode/kleider/paillettenkleider',
    'https://www.sheego.de/damenmode/kleider/shirtkleider', 'https://www.sheego.de/damenmode/kleider/spitzenkleider',
    'https://www.sheego.de/damenmode/kleider/strickkleider', 'https://www.sheego.de/damenmode/bademode/badeanzuege',
    'https://www.sheego.de/damenmode/bademode/badekleider', 'https://www.sheego.de/damenmode/bademode/bikinis',
    'https://www.sheego.de/damenmode/bademode/mixkinis', 'https://www.sheego.de/damenmode/bademode/strandbekleidung',
    'https://www.sheego.de/damenmode/bademode/tankinis', 'https://www.sheego.de/damen-waesche/bhs/alle-bhs',
    'https://www.sheego.de/damen-waesche/bhs/balconette-bhs', 'https://www.sheego.de/damen-waesche/bhs/bhs-ohne-buegel',
    'https://www.sheego.de/damen-waesche/bhs/entlastung-bhs', 'https://www.sheego.de/damen-waesche/bhs/buegel-bhs',
    'https://www.sheego.de/damen-waesche/bhs/minimizer-bhs', 'https://www.sheego.de/damen-waesche/bhs/push-up-bhs',
    'https://www.sheego.de/damen-waesche/bhs/schalen-bhs', 'https://www.sheego.de/damen-waesche/bhs/spitzen-bhs',
    'https://www.sheego.de/damen-waesche/bhs/sport-bhs', 'https://www.sheego.de/damen-waesche/bhs/t-shirt-bhs',
    'https://www.sheego.de/damen-waesche/bodies', 'https://www.sheego.de/damen-waesche/dessous',
    'https://www.sheego.de/damen-waesche/hochzeitsdessous', 'https://www.sheego.de/damen-waesche/homewear',
    'https://www.sheego.de/damen-waesche/pants', 'https://www.sheego.de/damen-waesche/nachthemden',
    'https://www.sheego.de/damen-waesche/schlafanzuege-pyjamas', 'https://www.sheego.de/damen-waesche/shapewear',
    'https://www.sheego.de/damen-waesche/slips', 'https://www.sheego.de/damen-waesche/strumpfhosen',
    'https://www.sheego.de/damen-waesche/socken', 'https://www.sheego.de/damen-waesche/unterhemden',
    'https://www.sheego.de/sale/blusen-tuniken', 'https://www.sheego.de/sale/jacken-maentel',
    'https://www.sheego.de/sale/jeans-hosen', 'https://www.sheego.de/sale/kleider-roecke',
    'https://www.sheego.de/sale/pullover-strickjacken', 'https://www.sheego.de/sale/schuhe-accessoires',
    'https://www.sheego.de/sale/shirts-tops', 'https://www.sheego.de/sale/sportbekleidung',
    'https://www.sheego.de/sale/waesche-bademode', 'https://www.sheego.de/sale/__groesse-44',
    'https://www.sheego.de/sale/__groesse-46', 'https://www.sheego.de/sale/__groesse-48',
    'https://www.sheego.de/sale/__groesse-50', 'https://www.sheego.de/sale/__groesse-52',
    'https://www.sheego.de/sale/__groesse-54', 'https://www.sheego.de/sale/__groesse-56',
    'https://www.sheego.de/sale/__groesse-58']
            
    def parse(self, response):
        for cloth in response.css('section.cj-product.js-product-box.js-product-box--list.js-unveil-plbox.at-product-box'):
            item = {
                    'title': cloth.css('div.product__title.at-pl-item-title::text').extract_first(),
                    'price': cloth.css('span.product__price--normal.l-bold.l-mr-5::text').extract_first(),
                    'image_url': cloth.css('img.cj-product__image.js-unveil-plbox-child.at-pl-item-image::attr(data-src)').extract_first()
            }
            yield ImageItem(title = item['title'], price = item['price'], image_urls = ['https:'+item['image_url']])
