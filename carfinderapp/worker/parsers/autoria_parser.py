# -*- coding: utf-8 -*-

import time
import json
import http.client

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

    def get_manufacturers(self):
        self.driver.get('https://auto.ria.com')
        dropdown = self.driver.find_elements_by_css_selector("#mainSearchForm > div.wrapper > div.item-column.primary-column > div:nth-child(2) > div > div.m-indent")
        dropdown[0].click()
        items = self.driver.find_elements_by_css_selector("#brandTooltipBrandAutocomplete-brand > ul > li > a")

        for item in items:
            print(item.text, item.get_attribute('data-value'))
            self.manufacturers[item.text.lower()] = item.get_attribute('data-value')

        return self.manufacturers

    def get_models_for_manufacturer(self, manufacturer_id):

        conn = http.client.HTTPSConnection('auto.ria.com')
        conn.request("GET", "/api/categories/1/marks/%s/models/_active/_with_count?langId=2" % str(manufacturer_id))

        r1 = conn.getresponse()
        data = r1.read()

        models_json = json.loads(data)

        return models_json

        # self.get_manufacturers()
        #
        # self.driver.get('https://auto.ria.com')
        # dropdown = self.driver.find_elements_by_css_selector("#mainSearchForm > div.wrapper > div.item-column.primary-column > div:nth-child(2) > div > div.m-indent")
        # dropdown[0].click()
        # # items = self.driver.find_elements_by_css_selector("#brandTooltipBrandAutocomplete-brand > ul > li > a")
        #
        #
        #
        # li_items = self.driver.find_elements_by_css_selector("#brandTooltipBrandAutocomplete-brand > ul > li")
        #
        # manufacturer_id = self.manufacturers.get(manufacturer.lower())
        # print('look for', manufacturer_id)
        #
        # for item in li_items:
        #     print(item.get_attribute('data-value'))
        #     if item.get_attribute('data-value') == manufacturer_id:
        #         item.click()
        #         print('Clicked item', manufacturer_id)
        #         break
        # time.sleep(3)
        #
        #
        # models_selector = self.driver.find_elements_by_css_selector("#mainSearchForm > div.wrapper > div.item-column.primary-column > div:nth-child(3)")
        # models_selector[0].click()
        #
        # model_items = self.driver.find_elements_by_css_selector("#brandTooltipBrandAutocomplete-model > ul > li > a")
        # print(model_items)
        # for model_item in model_items:
        #     print(model_item.get_attribute('data-value'), model_item.text)

        # TODO Finish get_manufacturers and  get_models_for_manufacturer