# -*- coding: utf-8 -*-

""" Worker exetutes next operations:
    1- Obtains a list of snoops from DB
    2- Create a parser for each snoop
    3- Runs parsers
"""

from parsers.autoria_parser import AutoRiaParser
from datastore.datastore import SQLAlchemyAdapter

parser_classes = [AutoRiaParser, ]

def get_parsers(**kwargs):
    parsers = []
    for cls in parser_classes:
        parsers.append(cls(**kwargs))

    return parsers


def get_snoops_from_db():
    ds = SQLAlchemyAdapter()
    db_snoops = ds.getSnoops()

    parsers = []
    for db_snoop in db_snoops:
        ar_parser = AutoRiaParser(db_snoop)
        parsers.append(ar_parser)
        # rst_parser = RSTParser(db_snoop)      # TODO add rst parser
        # self.parsers.append(rst_parser)
    return parsers

def find_new_cars():
    parsers = get_snoops_from_db()
    for parser in parsers:
        parser.get_cars()


if __name__ == "__main__":
    find_new_cars()



