__author__ = 'Modulus'


from mongoengine import *
from models.user import User


connect("tutorial")


class Message(Document):

    subject = StringField()
    text = StringField()
    receiver = ReferenceField(User)
    sender = ReferenceField(User)
