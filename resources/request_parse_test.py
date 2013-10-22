from datetime import datetime
from flask.ext.restful import Resource, marshal_with, reqparse, fields, abort

from models.user import User

__author__ = 'Modulus'

fields = {
    "firstName": fields.String,
    "lastName": fields.String,
    "userName": fields.String

}


class RequestParseTest(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('first_name', type=str, help="First name is needed")
        self.parser.add_argument("last_name", type=str, help="Last name is needed")
        self.parser.add_argument("user_name", type=str, help="User name is needed")
        self.parser.add_argument("birth_date", type=str, help="Your birthdate")
        self.parser.add_argument("pass", type=str, help="Password is needed")
        self.args = self.parser.parse_args()

    @marshal_with(fields)
    def post(self):

        first_name = self.args["first_name"]
        last_name = self.args["last_name"]
        user_name = self.args["user_name"]
        birth_date = self.args["birth_date"]
        passwd = self.args["pass"]

        existingUser = User.objects.get(firstName=first_name)

        if not existingUser or existingUser.userName != user_name:
            user = User(firstName=first_name, lastName=last_name, userName=user_name,
                birthDate=birth_date, passHash=passwd)
            user.save()
            return user

        else:
            abort(500)

