# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "autoria_cars"

    def start_requests(self):
        urls = ['https://auto.ria.com/search/?category_id=1&marka_id[0]=75&model_id[0]=663&s_yers[0]=2008&po_yers[0]=2010&currency=1&abroad=2&custom=1&fuelRatesType=city&engineVolumeFrom=&engineVolumeTo=&power_name=1&raceTo=130&countpage=10',
            #'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse_car_page(self, response):
        page = response.url
        self.log('###################### ' + page)
        return {'page': page}



    def parse(self, response):

        car_sections = response.css('.ticket-item')

        for car_section in car_sections:
            car_link = car_section.css('.hide').xpath('@data-link-to-view').extract_first()

            self.log('Found '+ car_link)
            yield scrapy.Request('https://auto.ria.com' + car_link, callback=self.parse_car_page)


        next_page = response.css('.js-next').xpath('@href').extract_first()
        self.log('**************')
        self.log(response.css('a'))
        if next_page is not None:
            next_page = response.urljoin(next_page)
            self.log(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            self.log('###')

