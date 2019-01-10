# -*- coding: utf-8 -*-

from parsers.autoria_parser import AutoRiaParser
from datastore import SQLiteDatastore

class BaseWorker(object):
    # Get all snoops
    # For each snoop update car list
    def find_new_cars(self):
        raise NotImplementedError


class Worker(BaseWorker):
    def __init__(self):
        self.ds = SQLiteDatastore()
        self.parsers = []

    def _get_snoops_from_db(self):
        db_snoops = self.ds.getSnoops()

        for db_snoop in db_snoops:
            ar_parser = AutoRiaParser(db_snoop)
            self.parsers.append(ar_parser)
            # rst_parser = RSTParser(db_snoop)      #Not implemented
            # self.parsers.append(rst_parser)

    def find_new_cars(self):
        self._get_snoops_from_db()
        for parser in self.parsers:
            parser.get_cars()



if __name__ == "__main__":
    worker = Worker()
    worker.find_new_cars()



