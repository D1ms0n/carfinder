"""This script obtains a list of manufacturers and related models"""

from parsers.autoria_parser import AutoRiaParser
from datastore.datastore import SQLAlchemyAdapter

parser_classes = [AutoRiaParser, ]

ds = SQLAlchemyAdapter()

def get_parsers(**kwargs):
    parsers = []
    for cls in parser_classes:
        parsers.append(cls(**kwargs))

    return parsers


def load_manufacturers_and_models(self):
    parsers = get_parsers()

    for parser in parsers:
        manufacturers = parser.get_manufacturers()

        for name in manufacturers:
            print('Create manufacturer', name)
            id = manufacturers[name]
            manufacturer = ds.create('ManufacturerId', manufacturer = name, autoria_id = id)
            models = parser.get_models_for_manufacturer(id)
            for model in models:
                print('Create manufacturer', model['name'])
                ds.create('ModelId', model=model['name'], autoria_id=model['value'])    # TODO add related manufacturer

