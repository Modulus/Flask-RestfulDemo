__author__ = 'Modulus'
from flask.ext.restful import Resource, Api, fields, marshal_with


from models.message import Message


class MessageResource(Resource):
    @marshal_with(Message.format())
    def get(self, id):
        return Message.objects.get(id=id)




