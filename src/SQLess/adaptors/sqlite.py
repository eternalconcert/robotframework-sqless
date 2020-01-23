import sqlite3


class SQLiteAdaptor:

    def __init__(self, **config):
        self.database = config['db']

    def _get_connection_and_cursor(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        return (connection, cursor)

    def _make_list(self, result, fieldnames):
        result_list = []
        for item in result:
            result_list.append(dict(zip(fieldnames, item)))
        return result_list

    def get_all(self, tablename, fields):
        connection, cursor = self._get_connection_and_cursor()
        cursor.execute("SELECT %s FROM %s" % (', '.join(fields.keys()), tablename))
        result = self._make_list(cursor.fetchall(), fields.keys())
        return result

    def get_by_filter(self, tablename, fields, **filters):
        connection, cursor = self._get_connection_and_cursor()
        filter = " AND ".join(f"{key}='{value}'" for key, value in filters.items())
        cursor.execute("SELECT %s FROM %s WHERE %s" % (', '.join(fields.keys()) ,tablename, filter))
        result = self._make_list(cursor.fetchall(), fields.keys())
        return result
