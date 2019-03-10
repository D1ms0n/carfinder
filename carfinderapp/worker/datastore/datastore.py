# -*- coding: utf-8 -*-

import sqlite3
import psycopg2
import sys
import pprint

# sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

CAR_TABLE_NAME = 'cars'
SNOOP_TABLE_NAME = 'snoops'


class BaseDatastore(object):
    def get_cars(self, *args, **kwargs):
        raise NotImplementedError

    def create_car(self, *args, **kwargs):
        raise NotImplementedError

    def get_snoops(self, *args, **kwargs):
        raise NotImplementedError

    def get_snoops(self, *args, **kwargs):
        raise NotImplementedError

    def create_snoop(self, *args, **kwargs):
        raise NotImplementedError

class SQLAlchemyAdapter(BaseDatastore):
    def __init__(self):
        Base = automap_base()

        engine = create_engine("sqlite:///../../db.sqlite3")

        # reflect the tables
        Base.prepare(engine, reflect=True)

        self.Snoop = Base.classes.carfinderapp_snoop
        self.Car = Base.classes.carfinderapp_car
        self.ManufacturerId = Base.classes.carfinderapp_manufacturerid
        self.ModelId = Base.classes.carfinderapp_modelid

        self.session = Session(engine)

    def _get_cls(self, cls_name):
        cl = self.__dict__.get(str(cls_name))
        return cl

    def get(self, cls_name, **kwargs):
        cl = self._get_cls(cls_name)

        entries = self.session.query(cl).filter_by(**kwargs).all()
        return entries

    def create(self, cls_name, **kwargs):
        cl = self._get_cls(cls_name)

        new_entry = cl(**kwargs)
        self.session.add(new_entry)
        self.session.commit()
        return new_entry

    def delete(self, cls_name, **kwargs):
        entries = self.get(cls_name, **kwargs)
        for entry in entries:
            self.session.delete(entry)
        self.session.commit()


class SQLDatastore(BaseDatastore):

    def _construct_create_query(self, table_name, columns, values):
        query = "INSERT INTO %s (%s) VALUES %s" % (table_name, ', '.join(columns), str(tuple(values)))
        return query


    def _create_record(self, table_name, **kwargs):
         query = self._construct_create_query()


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
                 ('%s', '%s', %d, %d , '%s', '%s')"""                                 # TODO CHANGE IT!!!

        self.cursor.execute(sql % (manufacturer, model, year, mileage,  url, color))
        self.conn.commit()
        # print('Datastore: Create car')

    def _get_records(self, table_name, columns = ['*'], **kwargs):
        self.cursor = self.conn.cursor()
        coumns_str = ','.join(columns)

        query = "SELECT %s FROM %s" % (coumns_str, table_name)

        query_args_list = ["%s = '%s'" % (k, v) for k, v in kwargs.items()]

        if query_args_list:
            query_args = " AND ".join(query_args_list)
            query = query + " WHERE " + query_args

        self.cursor.execute(query)

        records = self.cursor.fetchall()
        return records

    def _construct_updade_query(self, table_name, columns, values, **kwargs):
        query = "UPDATE %s " % table_name

        print(dict(zip(['a','b'], [1,2])).items())

        set_values_list = ["%s = '%s'" % (k, v) for k, v in dict(zip(columns, values)).items()]

        if set_values_list:
            set_args = " , ".join(set_values_list)
            query += " SET " + set_args

        query_args_list = ["%s = '%s'" % (k, v) for k, v in kwargs.items()]

        if query_args_list:
            query_args = " AND ".join(query_args_list)
            query += " WHERE " + query_args

        return query

    def _update_records(self, tablename, columns, values, **kwargs):
        self.cursor = self.conn.cursor()
        query = self._construct_updade_query(tablename, columns, values, **kwargs)
        if query:
            self.cursor.execute(query)
            self.conn.commit()
        else:
            raise Exception("Cannot construct updade query")

    def _create_update_records(self, tablename, columns, values, **kwargs):
        records = self._get_records(tablename, columns, **kwargs)
        if not records:
            _crea

    def _delete_records(self, table_name, **kwargs):
        self.cursor = self.conn.cursor()

        query = "DELETE FROM %s" % table_name

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

    def get_manufacturer_id(self, **kwargs):
        return self._get_records('carfinderapp_manufacturerid', **kwargs)



    def get_model_id(self, **kwargs):
        return self._get_records('carfinderapp_modelid', **kwargs)

    def create_update_manufacturer_id(self, manufacturer, **kwargs):
        ids = self.get_manufacturer_id(manufacturer=manufacturer)




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

