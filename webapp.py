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

    def run(self):
        self.app.run("127.0.0.1", debug=True, port=8100, ssl_context="adhoc")

if __name__ == "__main__":
    app = WebApp()
    app.run()

