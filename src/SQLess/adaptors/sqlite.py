import sqlite3

from robot.api import logger


class DatabaseCursor:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, *args):
        self.connection.commit()
        self.connection.close()


class SQLiteAdaptor:

    def __init__(self, **config):
        self.database = config['db']

    def _make_list(self, result, fieldnames):
        result_list = []
        for item in result:
            result_list.append(dict(zip(fieldnames, item)))
        return result_list

    def get_all(self, tablename, fields):
        with DatabaseCursor(self.database) as cursor:
            cursor.execute("SELECT %s FROM %s" % (', '.join(fields.keys()), tablename))
            result = self._make_list(cursor.fetchall(), fields.keys())
        return result

    def get_by_filter(self, tablename, fields, **filters):
        with DatabaseCursor(self.database) as cursor:
            filter = " AND ".join(f"{key}='{value}'" for key, value in filters.items())
            cursor.execute("SELECT %s FROM %s WHERE %s" % (', '.join(fields.keys()) ,tablename, filter))
            result = self._make_list(cursor.fetchall(), fields.keys())
        return result
