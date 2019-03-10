# -*- coding: utf-8 -*-

import os
import time
import threading
from multiprocessing import Process

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# from datastore import SQLiteDatastore


class BaseParser(object):
    # Init parser
    # Get first page url
    # Open first page
    # Get pagination count
    # Get cars for each page
    # Save cars
    # Close parser
    def get_cars(self):
        raise NotImplementedError


class Parser(BaseParser):
    def __init__(self, **kwargs):
        # print('BaseParser: __init__:START')

        self.debug = kwargs.get('debug', False)
        self.brand = kwargs.get('brand')
        self.model = kwargs.get('model')
        self.max_year = kwargs.get('max_year')
        self.min_year = kwargs.get('min_year')

        self.manufacturers = dict()
        self.all_car_links = []

        #self.datastore = Datastore()

        # print('BaseParser: get_driver:START')
        # Deprecated driver
        # self.driver = webdriver.PhantomJS()
        # self.driver.set_window_size(1400, 1000)

        chrome_options = Options()
        if not self.debug:
            chrome_options.add_argument("--headless")

        # Driver for MacOS
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.datastore = Datastore()
        # Driver for ubuntu
        #return = webdriver.Chrome(chrome_options=chrome_options, executable_path='/usr/local/bin/chromedriver')

        # print('BaseParser:__init__:OK')


    def _get_page_url(self, **kwargs):
        # should be implemented in the concrete parser
        raise NotImplementedError

    def _get_page(self, url):
        self.driver.get(url)

    def _get_page_by_number(self, page_number, max_count = 50):
        url = self._get_page_url(page_number)
        self._get_page(url)

    def close(self):
        self.driver.close()

    def _get_pagination_count(self):
        # should be implemented in the concrete parser
        raise NotImplementedError

    def _get_cars_from_page(self, page_number):
        # should be implemented in the concrete parser
        raise NotImplementedError

    def get_cars(self):
        for page in range(1, self._get_pagination_count()+1):
            self._get_cars_from_page(page)
            
# ############################################################################
#
#
#     def save_car(self, *args, **kwargs):
#         manufacturer = kwargs.get('manufacturer')
#         model        = kwargs.get('model')
#         year         = kwargs.get('year')
#         mileage      = kwargs.get('mileage')
#         url          = kwargs.get('url')
#
#         self.datastore.createCar(manufacturer, model, year, mileage,  url)
#
#     def get_cars(self):
#         self.pages_count = self._get_pagination_count()
#         for page_number in self.pages_count:
#             self._get_cars_from_page(page_number)
#
#
#     # @timeit
#     def get_car_urls_multithread(self):
#         # 139927.55 ms
#
#         threads = []
#         #for page_number in range(0, self.pagination_count):  # CHANGE self.pagination_count!!!
#         for page_number in range(0, 3):  # CHANGE self.pagination_count!!!
#             t = threading.Thread(target=self.get_cars_from_page, args=(page_number,))
#             print('Start thread %d' % page_number)
#             t.start()
#             threads.append(t)
#
#         for t in threads:
#             t.join()
#
#         print('Got %d cars links' % len(self.all_car_links))
#
#     # @timeit
#     def get_car_urls_multiproc(self):
#         threads = []
#         for page_number in range(0, self.pagination_count):  # CHANGE self.pagination_count!!!
#             t = Process(target=self.get_cars_from_page, args=(page_number,))
#             print('Start thread %d' % page_number)
#             t.start()
#             threads.append(t)
#
#         for t in threads:
#             t.join()
#
#         print('Got %d cars links' % len(self.all_car_links))
#
#     # @timeit
#     def get_car_urls_single_thread(self):
#         # 425606.68 ms
#         for page_number in range(0, self.pagination_count):  # CHANGE self.pagination_count!!!
#             self.get_cars_from_page(page_number)
#
#         print('Got %d cars links' % len(self.all_car_links))

