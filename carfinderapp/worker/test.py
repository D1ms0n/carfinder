import unittest
from unittest.mock import MagicMock

from datastore.datastore import SQLiteDatastore
from parsers.autoria_parser import AutoRiaParser

class TestAutoRiaParser(unittest.TestCase):

    def setUp(self):
        self.parser = AutoRiaParser(brand=9, model=96)

    def test__get_first_page_url(self):
        url = self.parser._get_page_url(page = 0, brand = 9, model= 96)
        self.assertEqual(url, 'https://auto.ria.com/search/?categories.main.id=1&brand.id[0]=9&model.id[0]=96&page=0&size=50')

    def test__get_pagination_count(self):
        self.parser._get_pagination_count()
        self.assertEqual(self.parser.pagination_count, 25)

    def test__get_cars_from_page(self):
        self.parser._get_cars_from_page(0)
        car_links = self.parser.all_car_links
        self.assertEqual(len(car_links), 50)

    def tearDown(self):
        self.parser.close()

class TestSQLiteDatastore(unittest.TestCase):
    def setUp(self):
        self.ds = SQLiteDatastore()

    def test_create_car(self):
        car_args = {'manufacturer':'0', 'model':'0', 'year':1881, 'mileage':777, 'color': 'red', 'url':'http://test.tst/car/testcar'}
        self.ds.create_car(**car_args)

        test_cars = self.ds.get_cars(url = 'http://test.tst/car/testcar')
        self.assertTrue(len(test_cars) == 1)

    def test_get_car_links(self):
        car_args = {'manufacturer': '0', 'model': '0', 'year': 1881, 'mileage': 777, 'color': 'red',
                    'url': 'http://test.tst/car/testcar'}
        self.ds.create_car(**car_args)

        car_args = {'manufacturer': '0', 'model': '0', 'year': 1881, 'mileage': 778, 'color': 'red',
                    'url': 'http://test.tst/car/testcar'}
        self.ds.create_car(**car_args)

        car_links = self.ds.get_cars(columns=['url',])
        self.assertEqual(car_links, [('http://test.tst/car/testcar',), ('http://test.tst/car/testcar',)])

    def test_delete_cars(self):
        test_cars = self.ds.get_cars(url='http://test.tst/car/testcar')
        self.ds.delete_cars(url = 'http://test.tst/car/testcar')

        test_cars = self.ds.get_cars(url = 'http://test.tst/car/testcar')

        self.assertTrue(len(test_cars) == 0)

    def tearDown(self):
        self.ds.delete_cars(url='http://test.tst/car/testcar')

class TestWorker(unittest.TestCase):
    def setUp(self):
        self.worker = Worker()

if __name__ == '__main__':
    unittest.main()