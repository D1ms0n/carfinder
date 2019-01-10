# -*- coding: utf-8 -*-

import sqlite3
import psycopg2
import sys
import pprint

CAR_TABLE_NAME = 'cars'
SNOOP_TABLE_NAME = 'snoops'


class BaseDatastore(object):
    def get_cars(self, *args, **kwargs):
        raise NotImplementedError

    def create_car(self, *args, **kwargs):
        raise NotImplementedError

    def get_snoops(self, *args, **kwargs):
        raise NotImplementedError

    def getSnoops(self, *args, **kwargs):
        raise NotImplementedError

    def createSnoop(self, *args, **kwargs):
        raise NotImplementedError


class SQLDatastore(BaseDatastore):
    def create_car(self, *args, **kwargs):
        url = kwargs.get('url')
        manufacturer = kwargs.get('manufacturer')
        model = kwargs.get('model')
        year = kwargs.get('year')
        mileage = kwargs.get('mileage')
        color = kwargs.get('color')

        self.cursor = self.conn.cursor()
        
        # execute our Query
        sql = """INSERT INTO carfinderapp_car
                 (manufacturer, model, year, mileage,  url, color) 
                 VALUES 
                 ('%s', '%s', %d, %d , '%s', '%s')"""                                 # CHANGE IT!!!

        self.cursor.execute(sql % (manufacturer, model, year, mileage,  url, color))
        self.conn.commit()
        # print('Datastore: Create car')


    def _get_records(self, table_name, columns = ['*'], **kwargs):
        self.cursor = self.conn.cursor()
        coumns_str = ','.join(columns)

        query = 'SELECT %s FROM %s' % (coumns_str, table_name)

        query_args_list = ['%s = "%s"' % (k, v) for k, v in kwargs.items()]

        if query_args_list:
            query_args = ' AND '.join(query_args_list)
            query = query + ' WHERE ' + query_args

        self.cursor.execute(query)

        records = self.cursor.fetchall()
        return records

    def _delete_records(self, table_name, **kwargs):
        self.cursor = self.conn.cursor()

        query = 'DELETE FROM %s' % table_name

        query_args_list = ['%s = "%s"' % (k, v) for k, v in kwargs.items()]

        if query_args_list:
            query_args = ' AND '.join(query_args_list)
            query = query + ' WHERE ' + query_args

        self.cursor.execute(query)
        self.conn.commit()

    def get_cars(self, columns = ['*'], *args, **kwargs):
        return self._get_records('carfinderapp_car', columns, **kwargs)

    def get_snoops(self, *args, **kwargs):
        return self._get_records('carfinderapp_snoop', **kwargs)

    def delete_cars(self, **kwargs):
        self._delete_records('carfinderapp_car', **kwargs)

    def delete_snoops(self, **kwargs):
        self._delete_records('carfinderapp_snoop', **kwargs)

class SQLiteDatastore(SQLDatastore):
    def __init__(self):
        self.conn = sqlite3.connect('../../db.sqlite3')

class PSDatastore(SQLDatastore):
    def __init__(self):
        conn_string = "host='localhost' dbname='postgres' user='postgres' password='nopasaran'"

        # print("Create datastore %d" % id)

        # get a connection, if a connect cannot be made an exception will be raised here
        self.conn = psycopg2.connect(conn_string)

        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        self.cursor = self.conn.cursor()


# if __name__ == "__main__":
#     datastore = Datastore()
#
#     datastore.createCar('Mers', 'G63', 1991, 130, 'http://ldld.kd')
#     datastore.getCar()

