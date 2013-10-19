__author__ = 'Modulus'

from flask.ext.restful import Resource, Api, fields, marshal_with


from models.user import User


class UserResource(Resource):

    @marshal_with(User.format())
    def get(self, id):
        return User.objects.get(id=id)

    def put(self, user):
        User.save(user)
        return user
