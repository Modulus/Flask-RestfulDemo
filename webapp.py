__author__ = 'JohnSigvald'


from flask import Flask
from flask.ext import restful

from resources.user_resource import UserResource
from resources.main import Main
from resources.user_list import UserList


class WebApp():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = restful.Api(self.app)

        self.api.add_resource(Main, "/")
        self.api.add_resource(UserResource, "/user/<string:id>")
        self.api.add_resource(UserList, "/users")

    def run(self, debug=False):
        self.app.run(debug=debug)

if __name__ == "__main__":
    app = WebApp()
    app.run(True)

