__author__ = 'Modulus'
from flask.ext.restful import Resource, Api, fields, marshal_with
from models.message import Message


class MessagesResource(Resource):


    @marshal_with(Message.format())
    def get(self, user_id):
        return list(Message.objects.all())




