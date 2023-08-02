import os
from datetime import datetime
from peewee import (SqliteDatabase, Model, DateTimeField, IntegerField, ForeignKeyField, CharField)


db = SqliteDatabase(os.path.abspath('users_data.db'))


class MainModel(Model):
    created_at = DateTimeField(default=datetime.now())

    class Meta:
        database = db


class UsersList(MainModel):
    from_user_id = IntegerField(primary_key=True)
    user_name = CharField()
    last_request = CharField(default='None|None|None')


class Requests(MainModel):
    user = ForeignKeyField(UsersList, backref='requests')
    request = CharField()


class TrainingDiary(MainModel):
    user = ForeignKeyField(UsersList, backref='records')
    journal_entry = CharField()


def create_tables():
    db.create_tables(MainModel.__subclasses__())
