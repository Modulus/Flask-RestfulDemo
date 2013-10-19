from resources.user_resource import UserResource

__author__ = 'JohnSigvald'


from flask import Flask
from flask.ext import restful
from resources.user_list_resource import UserListResource
from resources.messages_resource import MessagesResource


from resources.main import Main


class WebApp():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = restful.Api(self.app)

        self.api.add_resource(Main, "/")
        self.api.add_resource(UserResource, "/user/<string:id>")
        self.api.add_resource(UserListResource, "/users")
        self.api.add_resource(MessagesResource, "/messages/<string:user_id>")

    def run(self, debug=False):
        self.app.run(debug=debug)

if __name__ == "__main__":
    app = WebApp()
    app.run(True)

