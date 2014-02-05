from resources.image_resource import  ImageCustomResource
from resources.user_resource import UserResource
from views.index import IndexPage

__author__ = 'Modulus'


from flask import Flask, url_for, render_template
from flask.ext import restful
from resources.user_list_resource import ImageResource
from resources.messages_resource import MessagesResource

class MyWebApp(object):

    app = Flask(__name__)
    api = restful.Api(app)
    app.route("/", methods=["GET"])
    api.add_resource(UserResource, "/user/<string:id>", "/user")
    api.add_resource(ImageResource, "/users")
    api.add_resource(MessagesResource, "/messages/<string:user_id>")
    api.add_resource(ImageCustomResource, "/image", "/image/<string:id>")

    app.add_url_rule("/", view_func=IndexPage.as_view("index"))

    def run(self, debug=True, ssl=True):

        if ssl:
            self.app.run("127.0.0.1", debug=debug, ssl_context="adhoc")
        else:
            self.app.run(debug=debug)


# @app.route("/", methods=["GET"])
# def root():
#     return render_template("index.html", name=None)


if __name__ == "__main__":
    w = MyWebApp()
    w.run(True, True)



