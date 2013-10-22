from flask.ext.bcrypt import Bcrypt

__author__ = 'Modulus'
#coding: utf-8

from mongoengine import *
from datetime import datetime

from flask.ext.restful import Resource, Api, fields, marshal_with

connect("tutorial")


class User(Document):
    # def __init__(self, *args, **kwargs):
    #     super(User, self).__init__(args, kwargs)

    firstName = StringField(required=True, name="firstName")
    lastName = StringField(required=True, name="lastName")
    userName = StringField(required=True, name="userName")
    imagePath = FileField(name="imagePath")
    passHash = StringField(name="hash", required=True)
    birthDate = DateTimeField(name="birthDate", required=False)
    creationDate = DateTimeField(name="creationDate", default=datetime.now, required=True)

    def save(self, force_insert=False, validate=True, clean=True,
             write_concern=None,  cascade=None, cascade_kwargs=None,
             _refs=None, **kwargs):
        crypt = Bcrypt()
        hash = crypt.generate_password_hash(self.passHash)
        self.passHash = hash
        super(User, self).save()


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





