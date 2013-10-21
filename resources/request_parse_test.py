from flask.ext.restful import Resource, marshal_with, reqparse
from mongoengine import fields

__author__ = 'Modulus'

fields = {
    "name": fields.StringField

}


class RequestParseTest(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, help="Name is needed")



    @marshal_with(fields)
    def post(self):
        args = self.parser.parse_args()
        return {"name": args["name"]}
