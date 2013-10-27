from datetime import datetime
from bson import ObjectId
from flask import request, make_response
from flask.ext.restful import Resource, marshal_with, reqparse, fields, abort
import werkzeug
from models.Image import Image

from models.user import User

__author__ = 'Modulus'


class ImageCustomResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('image')
        self.args = self.parser.parse_args()

    @marshal_with(Image.format())
    def post(self):

        file = request.files["image"]

        image = Image()
        image.image = file
        image.image.content_type = "image/png"
        image.save()

        return "Image saved"

    def get(self, id):
        image = Image.objects.get(id=id)

        response = make_response(image.image.read())
        response.content_type = "image/png"

        return response
