__author__ = 'JohnSigvald'

from flask.ext import restful

from testdata import users


class UserResource(restful.Resource):
    def get(self, id):
        if not id:
            return {"message", "No user selected!"}
        else:
            data = users.Users()
            for user in data.get():
                if user["id"] == id:
                    return user
