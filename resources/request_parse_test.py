from datetime import datetime
from flask.ext.restful import Resource, marshal_with, reqparse
from mongoengine import fields, ValidationError
from models.user import User

__author__ = 'Modulus'

fields = {
    "firstName": fields.StringField,
    "lastName": fields.StringField,
    "userName": fields.StringField

}


class RequestParseTest(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('first_name', type=str, help="First name is needed")
        self.parser.add_argument("last_name", type=str, help="Last name is needed")
        self.parser.add_argument("user_name", type=str, help="User name is needed")
        self.args = self.parser.parse_args()

    @marshal_with(User.format())
    def post(self):
        try:
            first_name = self.args["first_name"]
            last_name = self.args["last_name"]
            user_name = self.args["user_name"]

            user = User(firstName=first_name, lastName=last_name, userName=user_name, birthDate=datetime.utcnow())
            user.save()
            return user
        except ValidationError:
            return {"error": "Missing required fields"}

