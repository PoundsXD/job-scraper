"""Attempt to scrape a page."""

import scrapy


class ScrapeStackOverflowJobs(scrapy.Spider):
    """A broken spider."""
    name = "job_scrape"

    def start_requests(self):
        """Should request things, yet doesn't."""
        urls = [
            'https://stackoverflow.com/jobs'
        ]
        for url in urls:
            yield scrapy.Requests(url=url, callback=self.parse)

    def parse(self, response):
        """Yep this should in theory do something."""
        for item in response.css(''):

            yield{
                'name': item.css('-name ::text').extract(),
                'location': item.css('-location ::text').extract(),
                'date': item.css('-posted-date ::text').extract(),
                'title': item.css('job-link ::text').extract(),
                'link': item.css('job-link').extract()
            }
    #     page = response.url.split("/")[-2]
    #     filename = 'quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('saved file %s' % filename)
