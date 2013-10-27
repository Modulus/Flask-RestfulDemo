__author__ = 'Modulus'

from mongoengine import *
from models.user import User

from flask.ext.restful import Resource, Api, fields, marshal_with

connect("tutorial")


class Image(Document):

    image = FileField()


    @staticmethod
    def format():
        return { "image": fields.Raw}