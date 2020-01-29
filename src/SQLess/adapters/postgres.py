import psycopg2
from robot.api import logger

from .adapter import AbstractAdapter


class DatabaseCursor:
    def __init__(self, database_settings):
        self.connection = psycopg2.connect(**database_settings)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, *args):
        self.connection.commit()
        self.connection.close()


def make_select_partial(tablename, fields):
    return "SELECT %s FROM \"%s\"" % (', '.join(fields.keys()) ,tablename)


def make_delete_partial(tablename):
    return "DELETE FROM \"%s\"" % (tablename)


def make_single_filter_partial(filters):
    filter = " AND ".join(f"{key}='{value}'" for key, value in filters.items())
    return filter


def make_where_partial(filters):
    where_partial = ""
    if filters:
        if isinstance(filters, dict):
            filter = make_single_filter_partial(filters)
        if isinstance(filters, list):
            clauses = []
            for clause in filters:
                clauses.append(make_single_filter_partial(clause))
            filter = " OR ".join(clauses)
        where_partial = f"WHERE {filter}"
    return where_partial


def make_count_partial(tablename):
    return f"SELECT COUNT(*) FROM \"{tablename}\""


def make_update_partial(tablename, **attributes):
    settings = ", ".join([f"{key}='{value}'" for key, value in attributes.items()])
    return f"UPDATE {tablename} SET {settings}"


def make_list(result, fieldnames):
    result_list = []
    for item in result:
        result_list.append(dict(zip(fieldnames, item)))
    return result_list


class PostgresqlAdapter(AbstractAdapter):

    def __init__(self, **config):
        self.database_settings = config
        self.database_settings.pop('dbms')

    def execute_sql(self, query):
        with DatabaseCursor(self.database_settings) as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result

    def get_all(self, tablename, fields):
        with DatabaseCursor(self.database_settings) as cursor:
            query = make_select_partial(tablename, fields)
            cursor.execute(query)
            result = make_list(cursor.fetchall(), fields.keys())
        return result

    def get_by_filter(self, tablename, fields, **filters):
        select_partial = make_select_partial(tablename, fields)
        where_partial = make_where_partial(filters)
        query = f"{select_partial} {where_partial}"
        with DatabaseCursor(self.database_settings) as cursor:
            cursor.execute(query)
            result = make_list(cursor.fetchall(), fields.keys())
        return result

    def count(self, tablename, **filters):
        count_partial = make_count_partial(tablename)
        where_partial = make_where_partial(filters)
        query = f"{count_partial} {where_partial}"
        with DatabaseCursor(self.database_settings) as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
        return result[0]

    def create(self, tablename, fields, **attributes):
        keys = ", ".join(attributes.keys())
        values = ", ".join([f"'{value}'" for value in attributes.values()])
        query = f"INSERT INTO \"{tablename}\" ({keys}) VALUES ({values}) RETURNING id"
        with DatabaseCursor(self.database_settings) as cursor:
            cursor.execute(query)
            last_id = cursor.fetchone()[0]

        # SQLite does not support nested transactions
        # therefore another connection must be created
        with DatabaseCursor(self.database_settings) as cursor:
            result = self.get_by_filter(tablename, fields, id=last_id)[0]
        return result

    def delete_all(self, tablename, **filters):
        with DatabaseCursor(self.database_settings) as cursor:
            query = make_delete_partial(tablename, **filters)
            cursor.execute(query)

    def delete_by_filter(self, tablename, **filters):
        with DatabaseCursor(self.database_settings) as cursor:
            delete_partial = make_delete_partial(tablename)
            where_partial = make_where_partial(filters)
            cursor.execute(f"{delete_partial} {where_partial}")

    def update_all(self, tablename, **attributes):
        with DatabaseCursor(self.database_settings) as cursor:
            update_partial = make_update_partial(tablename, **attributes)
            cursor.execute(update_partial)

    def update_by_filter(self, tablename, filters, **attributes):
        with DatabaseCursor(self.database_settings) as cursor:
            update_partial = make_update_partial(tablename, **attributes)
            where_partial = make_where_partial(filters)
            cursor.execute(f"{update_partial} {where_partial}")
