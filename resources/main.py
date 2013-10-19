__author__ = 'Modulus'

from flask.ext import restful


class Main(restful.Resource):
    def get(self):
        return {"message": "Hello there stranger!"}