import datetime
from formencode import api

__author__ = 'JohnSigvald'
#coding: utf-8

from flask.ext.restful import Resource, Api, fields, marshal_with, reqparse


from models.user import User


class UserListResource(Resource):

    @marshal_with(User.format())
    def get(self):
        users = []
        for user in User.objects():
            users.append(user)
        return users

    def put(self, user):
        self.users.users.append(user)
