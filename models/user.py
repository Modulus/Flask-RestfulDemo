__author__ = 'Modulus'

from mongoengine import *

from datetime import datetime


connect("tutorial")


class User(Document):

    firstName = StringField()
    lastName = StringField()
    userName = StringField()
    passHash = StringField()
    birthDate = DateTimeField()
    creationDate = DateTimeField(default=datetime.now)


