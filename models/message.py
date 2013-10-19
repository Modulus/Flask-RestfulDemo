__author__ = 'Modulus'
#coding: utf-8


from mongoengine import *
from models.user import User

from flask.ext.restful import Resource, Api, fields, marshal_with


connect("tutorial")


class Message(Document):

    subject = StringField()
    text = StringField()
    receiver = ReferenceField(User)
    sender = ReferenceField(User)

    @staticmethod
    def format():
        return {
            "subject": fields.String,
            "text": fields.String,
            "sender": fields.String,
            "receiver": fields.String

        }
