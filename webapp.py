from resources.image_resource import  ImageCustomResource
from resources.user_resource import UserResource

__author__ = 'Modulus'


from flask import Flask, url_for, render_template
from flask.ext import restful
from resources.user_list_resource import ImageResource
from resources.messages_resource import MessagesResource

app = Flask(__name__)
api = restful.Api(app)
app.route("/", methods=["GET"])
api.add_resource(UserResource, "/user/<string:id>", "/user")
api.add_resource(ImageResource, "/users")
api.add_resource(MessagesResource, "/messages/<string:user_id>")
api.add_resource(ImageCustomResource, "/image", "/image/<string:id>")


@app.route("/", methods=["GET"])
def root():
    return render_template("index.html", name=None)


app.run(debug=True)

