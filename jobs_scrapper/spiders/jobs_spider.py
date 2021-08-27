import scrapy

from jobs_scrapper.items import JobItem


class JobsSpider(scrapy.Spider):  
    name = 'jobs_spider'
    allowed_domains = ['news.ycombinator.com']
    start_urls = ['https://news.ycombinator.com/jobs']

    def parse(self, response):
        for index, job in enumerate(response.css('tr.athing')):
            job_detail_item = {
                'title': job.css('a.storylink::text').extract_first(),
                'url': job.css('a.storylink::attr(href)').extract_first(),
                'website_name': job.css('span.sitestr::text').extract_first(),
                'age': response.css('span.age > a::text').extract()[index]
            }
            yield JobItem(
                title = job_detail_item['title'],
                url = job_detail_item['url'],
                website_name = job_detail_item['website_name'],
                age = job_detail_item['age']
            )

        next_page_url = response.css('a.morelink::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url = next_page_url, callback = self.parse)
