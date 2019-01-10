import unittest
from unittest.mock import MagicMock

from parsers.autoria_parser import AutoRiaParser
from datastore import SQLiteDatastore

from worker import Worker




    



    # def tearDown(self):

if __name__ == '__main__':
    unittest.main()



# from parsers.autoria_parser import AutoRiaParser
#
# parser = AutoRiaParser(brand=9, model= 96)
#
# parser.get_driver()
# parser.get_first_page_url()
# parser.get_first_page()
# parser.get_pagination_count()
# # parser.get_car_urls_multithread()
# parser.get_car_urls_multiproc()
#
# #parser.get_car_urls_multiproc()
# #parser.get_car_urls_single_thread()
#
# print(parser.first_page_url)
#
# parser.close()