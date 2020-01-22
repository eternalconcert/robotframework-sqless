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


Migration.migration_dir = os.path.join(os.getcwd(), 'utils/migrations')
migrations = Migration()
migrations.create_migrations()
migrations.run_migrations()


User.objects.get_or_create(username="TestUser1", email="somename@somedomain.tld")
User.objects.get_or_create(username="TestUser2", email="someothername@someotherdomain.tld")
