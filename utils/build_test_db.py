# This file is needed to initialize the models and migrations
import os
from nopea.dbobject import DbObject

from nopea import fields
from nopea.adaptors.sqlite import SQLiteAdaptor
from nopea.migrations import Migration


DbObject.adaptor = SQLiteAdaptor('sqless.db')


class User(DbObject):
    username = fields.CharField(max_length=20)
    email = fields.CharField(max_length=100)
    failed_logins = fields.IntegerField(default=0)


class Post(DbObject):
    user = fields.ForeignKey(User)
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
    {"user": 1, "title": "TestPosting", "content": "Lorem Ipsum Dolor Sit"}
]


for post in posts:
    Post.objects.get_or_create(**post)
