import datetime
from flask.ext.bcrypt import Bcrypt
from mongoengine import DoesNotExist

__author__ = 'Modulus'

from flask.ext.restful import Resource, Api, fields, marshal_with, abort, reqparse

from models.user import User


class UserResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("first_name", type=str, help="First name is required")
        self.parser.add_argument("last_name", type=str, help="Last name is required")
        self.parser.add_argument("user_name", type=str, help="User name is required")
        self.parser.add_argument("birth_date", type=datetime, help="Your birthday")
        self.parser.add_argument("pass", type=str, help="Password is required")
        self.parser.add_argument("id", type=str, help="User id")
        self.parser.add_argument("image")
        self.args = self.parser.parse_args()

    @marshal_with(User.format())
    def get(self, id):
        return User.objects.get(id=id)

    def put(self, user):
        User.save(user)
        return user

    @marshal_with(User.format())
    def post(self):

        first_name = self.args["first_name"]
        last_name = self.args["last_name"]
        user_name = self.args["user_name"]
        birth_date = self.args["birth_date"]
        passwd = self.args["pass"]
        image = self.args["image"]
        #Hashing is done on user save, see User class for this
        if passwd:
            try:
                existingUser = User.objects.get(firstName=first_name)
            except DoesNotExist:
                user = User(firstName=first_name, lastName=last_name, userName=user_name,
                            birthDate=birth_date, passHash=hash)
                user.save()
                return user
        #Don't inform of existing user
        if existingUser:
            abort(500)

    def delete(self):
        id = self.args["id"]
        if not id:
            abort(500)
        else:
            existingUser = User.objects.get(id=id)
            existingUser.delete()


