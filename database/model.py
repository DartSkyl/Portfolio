import os
from datetime import datetime
from peewee import (SqliteDatabase, Model, DateTimeField, IntegerField, ForeignKeyField, CharField)


db = SqliteDatabase(os.path.abspath('users_data.db'))  # DataBase


class MainModel(Model):
    """
    Main model. Has a common column for all inherited tables
    Attributes:
        created_at (DateTimeField): Date and time when the record was created
    """
    created_at: DateTimeField = DateTimeField(default=datetime.now())

    class Meta:
        """Class with database indication"""
        database: SqliteDatabase = db  # DataBase


class UsersList(MainModel):
    """
    User table. Contains ID in telegram, username and last request
    Attributes:
        from_user_id (int): ID in telegram
        user_name (str): first_name in telegram
        last_request (str): Last request
    """
    from_user_id: int = IntegerField(primary_key=True)
    user_name: str = CharField()
    last_request: str = CharField(default='None|None|None')


class Requests(MainModel):
    """
    Query table. Contains the user and the request itself. The record can be called by the backlink
    Attributes:
        user (UsersList): User from UsersList, backlink 'requests'
        request (str): String, with request parameters
    """
    user: UsersList = ForeignKeyField(UsersList, backref='requests')
    request: str = CharField()


class TrainingDiary(MainModel):
    """
     Table stores user entries made in the diary. The record can be called by the backlink
     Attributes:
         user (UsersList): User from UsersList, backlink 'records'
         journal_entry (str): A string with a user record
    """
    user: UsersList = ForeignKeyField(UsersList, backref='records')
    journal_entry: str = CharField()


def create_tables():
    """Function creates tables bsed on the models described above"""
    db.create_tables(MainModel.__subclasses__())
