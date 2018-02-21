import scrapy

class G1Spider(scrapy.Spider):
    name = "g1"
    start_urls = [
        'http://g1.globo.com/politica/'
    ]

    def parse(self, response):
        links = response.xpath('//div[@class="feed-text-wrapper"]//@href').extract()
        headlines = response.xpath('//div[@class="feed-text-wrapper"]//div[@class="_s"]//p/text()').extract()
        for link, headline in zip(links, headlines):
            yield {
                'link': link,
                'headline': headline
            }
        
        next_page = response.xpath('//div[@class="load-more gui-color-primary-bg"]//@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)




