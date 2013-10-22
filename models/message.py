__author__ = 'Modulus'
#coding: utf-8


from mongoengine import *
from models.user import User

from flask.ext.restful import Resource, Api, fields, marshal_with


connect("tutorial")


class Message(Document):

    subject = StringField(default="")
    text = StringField(required=True)
    receiver = ReferenceField(User)
    sender = ReferenceField(User, required=True)
    read = BooleanField()
    sent = DateTimeField()
    received = DateTimeField()

    @staticmethod
    def format():
        return {
            "subject": fields.String,
            "text": fields.String,
            "sender": fields.Nested(Message.userFormat()),
            "receiver": fields.Nested(Message.userFormat())
        }

    @staticmethod
    def userFormat():
        return {
            "firstName": fields.String,
            "lastName": fields.String,
            "userName": fields.String,
        }
