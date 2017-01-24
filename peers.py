from peewee import *

db = SqliteDatabase('peers.db')

class Peer(Model):
    name = CharField(max_length = 20)
    phone = IntegerField(unique=True)
    email = CharField(max_length = 60)

    class Meta:
        database = db


db.connect()
db.create_tables([Peer], safe=True)