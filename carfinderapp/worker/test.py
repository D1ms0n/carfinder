import unittest
from unittest.mock import MagicMock

from worker import Worker
from datastore.datastore import SQLiteDatastore, SQLAlchemyAdapter
from parsers.autoria_parser import AutoRiaParser

class TestAutoRiaParser(unittest.TestCase):

    def setUp(self):
        self.parser = AutoRiaParser(brand=9, model=96, debug=True)

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

    def test_get_manufacturers(self):
        self.parser.get_manufacturers()

    def test_get_models_for_manufacturer(self):
        self.parser.get_models_for_manufacturer('bmw')


    def tearDown(self):
        self.parser.close()

class TestSQLAlchemyAdapter(unittest.TestCase):
    def setUp(self):
        self.ds = SQLAlchemyAdapter()

    def test__get_cls(self):
        cl = self.ds._get_cls('Car')
        self.assertEqual(str(cl), "<class 'sqlalchemy.ext.automap.carfinderapp_car'>")
        cl = self.ds._get_cls('Snoop')
        self.assertEqual(str(cl), "<class 'sqlalchemy.ext.automap.carfinderapp_snoop'>")
        cl = self.ds._get_cls('ManufacturerId')
        self.assertEqual(str(cl), "<class 'sqlalchemy.ext.automap.carfinderapp_manufacturerid'>")
        cl = self.ds._get_cls('ModelId')
        self.assertEqual(str(cl), "<class 'sqlalchemy.ext.automap.carfinderapp_modelid'>")

    def test_create_car(self):
        car_args = {'manufacturer':'0', 'model':'0', 'year':1881, 'mileage':777, 'color': 'red',
                    'url':'http://test.tst/car/testcar'}
        car_list = self.ds.get('Car')
        new_car = self.ds.create('Car', **car_args)
        new_car_list = self.ds.get('Car')

        self.assertEqual(str(type(new_car)), "<class 'sqlalchemy.ext.automap.carfinderapp_car'>")
        self.assertEqual(len(car_list)+1,len(new_car_list))

    def test_get_car(self):
        car_args = {'manufacturer': '0', 'model': '0', 'year': 1881, 'mileage': 777, 'color': 'red',
                    'url': 'http://test.tst/car/test_get_car'}

        new_car = self.ds.create('Car', **car_args)
        car_list = self.ds.get('Car', url = 'http://test.tst/car/test_get_car')

        self.assertTrue(new_car in car_list)

    def test_delete_cars(self):
        car_args = {'manufacturer': '0', 'model': '0', 'year': 1881, 'mileage': 777, 'color': 'red',
                    'url': 'http://test.tst/car/test_get_car'}
        new_car = self.ds.create('Car', **car_args)

        self.ds.delete('Car', url = 'http://test.tst/car/testcar')

        car_list = self.ds.get('Car', url = 'http://test.tst/car/testcar')
        self.assertEqual(car_list, [])

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

    def test__construct_updade_query(self):
        query = self.ds._construct_updade_query('test_table',
                                                ['col1', 'col2'],
                                                ['val1', 'val2'],
                                                manufacturer = 'test_manufacturer')
        expected_query = "UPDATE test_table  SET col1 = 'val1' , col2 = 'val2' WHERE manufacturer = 'test_manufacturer'"

        self.assertEqual(query, expected_query)

    def test__construct_create_query(self):
        query = self.ds._construct_create_query('test_table', ['col1', 'col2'], ['val1', 'val2'])
        expected_query = "INSERT INTO test_table (col1, col2) VALUES ('val1', 'val2')"

        self.assertEqual(query, expected_query)

    def test__create_record(self):
        new_snoop = self.ds._create_record()

    def tearDown(self):
        self.ds.delete_cars(url='http://test.tst/car/testcar')

class TestWorker(unittest.TestCase):
    def setUp(self):
        self.worker = Worker()

    def test_load_manufacturers_and_models(self):
        self.worker.load_manufacturers_and_models()

if __name__ == '__main__':
    unittest.main()