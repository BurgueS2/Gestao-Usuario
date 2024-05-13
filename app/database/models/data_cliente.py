from peewee import Model, CharField, DateTimeField
from app.database.database import db
import datetime


class Cliente(Model):
    nome = CharField()
    email = CharField()
    data_creation = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
