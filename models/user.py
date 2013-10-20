__author__ = 'Modulus'
#coding: utf-8

from mongoengine import *
from datetime import datetime

from flask.ext.restful import Resource, Api, fields, marshal_with




connect("tutorial")


class User(Document):

    firstName = StringField()
    lastName = StringField()
    userName = StringField()
    imagePath = FileField()
    passHash = StringField()
    birthDate = DateTimeField()
    creationDate = DateTimeField(default=datetime.now)

    @staticmethod
    def format():
        return {
            "firstName": fields.String,
            "lastName": fields.String,
            "userName": fields.String,
            # "imagePath": fields.String,
            "passHash": fields.String,
            "birthDate": fields.DateTime,
            "creationDate": fields.DateTime

        }





