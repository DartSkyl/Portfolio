from datetime import datetime
from peewee import *


db = SqliteDatabase('request_history.db')


class RequestHistory(Model):
    create_at = DateField(default=datetime.now())
    request = TextField()

    class Meta:
        database = db


RequestHistory.create_table()
test = RequestHistory.create(request=...)
test_2 = RequestHistory.create(request=...)

print(datetime.now())