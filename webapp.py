from resources.request_parse_test import RequestParseTest
from resources.user_resource import UserResource

__author__ = 'JohnSigvald'


from flask import Flask, url_for, render_template
from flask.ext import restful
from resources.user_list_resource import UserListResource
from resources.messages_resource import MessagesResource



app = Flask(__name__)
api = restful.Api(app)
app.route("/", methods=["GET"])
# api.add_resource(Main, "/")
api.add_resource(UserResource, "/user/<string:id>")
api.add_resource(UserListResource, "/users")
api.add_resource(MessagesResource, "/messages/<string:user_id>")
api.add_resource(RequestParseTest, "/parse")


@app.route("/", methods=["GET"])
def root():
    return render_template("index.html", name=None)


app.run(debug=True)







    # def run(self, debug=False):
    #     self.app.run(debug=debug)

# if __name__ == "__main__":
#     app = WebApp()
#     app.run(True)

