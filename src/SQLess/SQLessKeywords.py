import os
import yaml

from robot.api import logger

from adaptors.sqlite import SQLiteAdaptor


class SQLessKeywords(object):
    ROBOT_LIBRARY_SCOPE = 'Global'

    def __init__(self, schema_defintion_path=None):
        self.schema_defintion_path = schema_defintion_path if schema_defintion_path else 'schema.yml'
        self.schema = self._read_schema()
        self.adaptor = self._get_adaptor()

    def _get_adaptor(self):
        if self.schema['database_config']['dbms'] == 'sqlite':
            adaptor = SQLiteAdaptor

        return adaptor(**self.schema['database_config'])

    def _read_schema(self):
        with open(self.schema_defintion_path) as file:
            schema_defintion = yaml.load(file, Loader=yaml.FullLoader)
        return schema_defintion

    def _get_tablename_and_fieldname(self, identifier):
        tablename = self.schema['schema'].get(identifier.lower())['tablename']
        fieldnames = self.schema['schema'].get(identifier.lower())['fields']
        return (tablename, fieldnames)

    def get_all(self, identifier):
        tablename, fieldnames = self._get_tablename_and_fieldname(identifier)
        return self.adaptor.get_all(tablename, fieldnames)

    def get_by_filter(self, identifier, **filters):
        tablename, fieldnames = self._get_tablename_and_fieldname(identifier)
        return self.adaptor.get_by_filter(tablename, fieldnames, **filters)
