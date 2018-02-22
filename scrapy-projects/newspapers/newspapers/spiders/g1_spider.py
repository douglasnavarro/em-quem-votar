import scrapy
from newspapers.items import ArticleItem

class G1Spider(scrapy.Spider):
    name = "g1"
    start_urls = [
        'http://g1.globo.com/politica/'
    ]

    root_words = [
        'Corrupção'
    ]

    words = []
    for root_word in root_words:
        words.append(root_word)
        words.append(root_word.lower())

    def parse(self, response):
        articles = response.xpath('//div[@class="feed-text-wrapper"]')
        for article in articles:
            headline = article.xpath('.//div[@class="_s"]//p/text()').extract_first()
            summary  = article.xpath('.//p[@class="feed-post-body-resumo"]/text()').extract_first()
            link     = article.xpath('.//a//@href').extract_first()
            if headline is not None and any(word in headline for word in self.words) or \
                summary is not None and any(word in summary for word in self.words):
                item = ArticleItem()
                item['headline'] = headline
                item['summary']  = summary
                item['link']     = link
                yield item
        next_page = response.xpath('//div[@class="load-more gui-color-primary-bg"]//@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)




