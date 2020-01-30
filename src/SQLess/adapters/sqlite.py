import sqlite3
from robot.api import logger

from .adapter import BaseAdapter


class DatabaseCursor:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, *args):
        self.connection.commit()
        self.connection.close()


class SQLiteAdapter(BaseAdapter):

    def __init__(self, **config):
        self.database_settings = config['db']
        self.database_cursor = DatabaseCursor

    @staticmethod
    def make_count_partial(tablename):
        return f"SELECT COUNT(*) FROM {tablename}"

    def create(self, tablename, fields, **attributes):
        keys = ", ".join(attributes.keys())
        values = ", ".join([f"'{value}'" for value in attributes.values()])
        query = f"INSERT INTO {tablename} ({keys}) VALUES ({values})"
        with self.database_cursor(self.database_settings) as cursor:
            cursor.execute(query)
            cursor.execute("""SELECT last_insert_rowid()""")
            last_id = cursor.fetchone()[0]

            cursor.connection.commit()
            result = self.get_by_filter(tablename, fields, id=last_id)[0]
        return result
