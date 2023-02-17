import scrapy


class JoblistSpider(scrapy.Spider):
    name = 'joblist'
    allowed_domains = ['realpython.github.io']
    start_urls = ['http://realpython.github.io/fake-jobs/']

    def parse(self, response):
        for jobs in response.css('div.card-content'):
            yield {
                'position': jobs.css('h2.title.is-5::text').get(),
                'company': jobs.css('h3.subtitle.is-6.company::text').get(),
                'location': jobs.css('p.location::text').get().replace('\n',''),
                'deadline': jobs.css('time::attr(datetime)').get(),
                'link': jobs.css('a.card-footer-item').attrib['href']
    
            }
