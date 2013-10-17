__author__ = 'JohnSigvald'


from flask.ext import restful


from testdata import users


class UserList(restful.Resource):



    def __init__(self):

        self.users = users.Users().users

    def get(self):
        return self.users

    def put(self, user):
        self.users.users.append(user)
