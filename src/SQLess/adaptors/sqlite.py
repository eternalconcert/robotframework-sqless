import sqlite3


class SQLiteAdaptor:

    def __init__(self, **config):
        self.database = config['db']

    def _get_connection_and_cursor(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        return (connection, cursor)

    def get_all(self, tablename, fieldnames):
        connection, cursor = self._get_connection_and_cursor()
        cursor.execute("SELECT %s FROM %s" % (', '.join(fieldnames.keys()), tablename))
        return cursor.fetchall()

    def get_by_filter(self, tablename, fieldnames, **filters):
        connection, cursor = self._get_connection_and_cursor()
        filter = " AND ".join(f"{key}='{value}'" for key, value in filters.items())
        cursor.execute("SELECT %s FROM %s WHERE %s" % (', '.join(fieldnames.keys()) ,tablename, filter))
        return cursor.fetchall()
