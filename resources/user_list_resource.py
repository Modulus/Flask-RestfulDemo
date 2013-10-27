import datetime
from formencode import api

__author__ = 'Modulus'
#coding: utf-8

from flask.ext.restful import Resource, Api, fields, marshal_with, reqparse


from models.user import User


class ImageResource(Resource):

    @marshal_with(User.format())
    def get(self):
        return list(User.objects.all())
