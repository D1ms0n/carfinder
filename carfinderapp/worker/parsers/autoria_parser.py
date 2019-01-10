# -*- coding: utf-8 -*-

import time

from parsers.base_parser import  Parser
# from datastore import SQLiteDatastore
# Base config
AUTORIA_BASE_URL   = 'https://auto.ria.com/'
AUTORIA_SEARCH_URL = 'https://auto.ria.com/search/?categories.main.id=1&brand.id[0]=%d&model.id[0]=%d&page=%d&size=%d'
page_size = 50


class AutoRiaParser(Parser):

    def _get_page_url(self, page = 0, max_count = 50, **kwargs):
        return AUTORIA_SEARCH_URL % (self.brand, self.model, page, 50)

    def _get_pagination_count(self):
        self.first_page = self._get_page_url()
        self._get_page(self.first_page)
        time.sleep(1)
        self.pagination_links = self.driver.find_elements_by_css_selector('a.page-link')

        self.pagination_count = int(self.pagination_links[-2].text) + 1

        # print('Got %d pagination urls' % self.pagination_count)

    def _get_cars_from_page(self, page_number):
        # print('START page %d' % page_number)
        self._get_page_by_number(page_number)
        time.sleep(1)

        car_links = self.driver.find_elements_by_css_selector('a.address')

        for link in car_links:
            url = link.get_attribute("href")
            if 'https://auto.ria.com/auto_' in url:
                self.all_car_links.append(url)

        # print('FINISH  page %d' % page_number)
