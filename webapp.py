from models.user import User

__author__ = 'Modulus'

from resources.image_resource import  ImageCustomResource
from resources.user_resource import UserResource
from views.index import IndexView
from views.login import LoginView

from flask import Flask, url_for, render_template, request
from flask.ext import restful
from flask.ext.login import LoginManager, login_user
from resources.user_list_resource import ImageResource
from resources.messages_resource import MessagesResource

app = Flask(__name__)
api = restful.Api(app)
loginManager = LoginManager()
loginManager.init_app(app)


class MyWebApp(object):

    api.add_resource(UserResource, "/user/<string:id>", "/user")
    api.add_resource(ImageResource, "/users")
    # api.add_resource(MessagesResource, "/messages/<string:user_id>")
    api.add_resource(MessagesResource, "/messages/", "/messages")
    api.add_resource(ImageCustomResource, "/image", "/image/<string:id>")

    app.add_url_rule("/", view_func=IndexView.as_view("index"))
    # app.add_url_rule("/login", view_func=LoginView.as_view("login"))
    #
    # @staticmethod
    # @app.route("/login", methods=["GET", "POST"])
    # @loginManager.login
    # def login():
    #     return "Whoop whoop"
    @staticmethod
    def login():
        request
        login_user()

    #Should return None and not raise an exception if invalid id has been used
    @staticmethod
    @loginManager.user_loader
    def load_user(userId):
        return User.objects.get(id=userId)

    def run(self, debug=True, ssl=True):

        if ssl:
            app.run("127.0.0.1", debug=debug, ssl_context="adhoc")
        else:
            app.run(debug=debug)


if __name__ == "__main__":
    w = MyWebApp()
    w.run(True, True)



