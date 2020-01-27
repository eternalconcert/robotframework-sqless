# This file is needed to initialize the models and migrations
import os
import sys

from nopea.dbobject import DbObject

from nopea import fields
from nopea.adaptors.mysql import MySQLAdaptor
from nopea.adaptors.postgres import PostgreSQLAdaptor
from nopea.adaptors.sqlite import SQLiteAdaptor
from nopea.migrations import Migration


if 'sqlite' in sys.argv:
    DbObject.adaptor = SQLiteAdaptor('sqless.db')

elif 'mysql' in sys.argv:
    DbObject.adaptor = MySQLAdaptor({
        'host': 'localhost',
        'user': 'sqless',
        'db': 'sqless',
        'use_unicode': True,
        'charset': 'utf8'
    })

elif 'postgres' in sys.argv:
    DbObject.adaptor = PostgreSQLAdaptor({
        'host': 'localhost',
        'user': 'sqless',
        'database': 'sqless',
        'password': 'sqless'
    })


class User(DbObject):
    username = fields.CharField(max_length=20)
    email = fields.CharField(max_length=100)
    failed_logins = fields.IntegerField(default=0)


class Post(DbObject):
    title = fields.CharField(max_length=100)
    content = fields.TextField()


Migration.migration_dir = os.path.join(os.getcwd(), 'utils/migrations')
migrations = Migration()
migrations.create_migrations()
migrations.run_migrations()


users = [
    {"username": "TestUser1", "email": "somename@somedomain.tld"},
    {"username": "TestUser2", "email": "someothername@someotherdomain.tld"},
    {"username": "TestUser3", "email": "another@mail.tld", "failed_logins": 12}
]


for user in users:
    User.objects.get_or_create(**user)


posts = [
    {"title": "TestPosting", "content": "Lorem Ipsum Dolor Sit"},
    {"title": "SomeOtherStuff", "content": "hello, world!"},
]


for post in posts:
    Post.objects.get_or_create(**post)
