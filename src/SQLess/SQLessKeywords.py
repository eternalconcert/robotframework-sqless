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
        """
        Helper method to get the correct adaptor

        """
        if self.schema['database_config']['dbms'] == 'sqlite':
            adaptor = SQLiteAdaptor

        return adaptor(**self.schema['database_config'])

    def _read_schema(self):
        """
        Reads the schema from the schema defintion file

        :returns: dict

        """
        with open(self.schema_defintion_path) as file:
            schema_defintion = yaml.load(file, Loader=yaml.FullLoader)
        return schema_defintion

    def _get_tablename_and_fieldname(self, identifier):
        tablename = self.schema['schema'].get(identifier.lower())['tablename']
        fieldnames = self.schema['schema'].get(identifier.lower())['fields']
        return (tablename, fieldnames)

    def get_all(self, identifier):
        """
        Dispatches the function call to the configured adaptor and returns all rows from the table
        identified by the `identifier`.

        The `identifier` must match a table defintion in the schema defintion file.

        Keyword usage example:
            ${users}   Get All    Users

        :returns: list of dicts
        example:
        [
            {
                'id': 1,
                'username': 'TestUser1'
            },
            ...
        }
        """
        tablename, fieldnames = self._get_tablename_and_fieldname(identifier)
        return self.adaptor.get_all(tablename, fieldnames)

    def get_by_filter(self, identifier, **filters):
        """
        Dispatches the function call to the configured adaptor and returns the rows from the table
        identified by the `identifier`, where the filter matches.

        The `identifier` must match a table defintion in the schema defintion file and the filter keys must
        match row names in the schema defintion file.

        Keyword usage example:
            ${users}   Get By Filter    Users    email=someothername@someotherdomain.tld

        :returns: list of dicts
        example:
        [
            {
                'id': 1,
                'username': 'TestUser1'
            },
            ...
        }
        """
        tablename, fieldnames = self._get_tablename_and_fieldname(identifier)
        return self.adaptor.get_by_filter(tablename, fieldnames, **filters)
