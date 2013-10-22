__author__ = 'Modulus'
#coding: utf-8

from mongoengine import *
from datetime import datetime

from flask.ext.restful import Resource, Api, fields, marshal_with

connect("tutorial")


class User(Document):

    firstName = StringField(required=True, name="First name")
    lastName = StringField(required=True, name="Last name")
    userName = StringField(required=True, name="User name")
    imagePath = FileField()
    passHash = StringField(name="Password")
    birthDate = DateTimeField(name="Birthdate")
    creationDate = DateTimeField(name="Creation date", default=datetime.now)

    @staticmethod
    def format():
        return {
            "firstName": fields.String,
            "lastName": fields.String,
            "userName": fields.String,
            "imagePath": fields.String,
            "passHash": fields.String,
            "birthDate": fields.DateTime,
            "creationDate": fields.DateTime

        }





