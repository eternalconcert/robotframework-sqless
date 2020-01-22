import os
import sqlite3

import yaml
from robot.api import logger


class SQLessKeywords(object):
    ROBOT_LIBRARY_SCOPE = 'Global'

    def __init__(self, schema_defintion_path=None):
        self.schema_defintion_path = schema_defintion_path if schema_defintion_path else 'schema.yml'
        self.schema = self._read_schema()

    def _get_connection_and_cursor(self):
        connection = sqlite3.connect(self.schema['database_config']['db'])
        cursor = connection.cursor()
        return connection, cursor

    def _read_schema(self):
        with open(self.schema_defintion_path) as file:
            schema_defintion = yaml.load(file, Loader=yaml.FullLoader)
        return schema_defintion

    def _get_tablename_and_fieldname(self, identifier):
        tablename = self.schema['schema'].get(identifier.lower())['tablename']
        fieldnames = self.schema['schema'].get(identifier.lower())['fields']
        return (tablename, fieldnames)

    def get_all(self, identifier):
        connection, cursor = self._get_connection_and_cursor()
        tablename, fieldnames = self._get_tablename_and_fieldname(identifier)
        cursor.execute("SELECT %s FROM %s" % (', '.join(fieldnames.keys()) ,tablename))
        return cursor.fetchall()

    def filter(self, identifier, **filters):
        connection, cursor = self._get_connection_and_cursor()
        tablename, fieldnames = self._get_tablename_and_fieldname(identifier)
        filter = ", ".join(f"{key}='{value}'" for key, value in filters.items())
        cursor.execute("SELECT %s FROM %s WHERE %s" % (', '.join(fieldnames.keys()) ,tablename, filter))
        return cursor.fetchall()
