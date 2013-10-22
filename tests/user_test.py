from flask.ext.bcrypt import Bcrypt
from resources.testdata.populator import Populator

__author__ = 'Modulus'

from models.user import User

from unittest import TestCase


class UserTest(TestCase):

    def setUp(self):

        self.pop = Populator()
        self.pop.run()

    def tearDown(self):

        self.pop.clear()

    def test_save(self):
        self.users = [User(), User(), User()]
        for index, user in enumerate(self.users):
            user.firstName = "User_"+str(index)
            user.lastName = "User_"+str(index)+"_lastName"
            user.userName = "UserName_"+str(index)
            user.passHash = user.userName

        for user in self.users:
            self.assertIsNone(user.id, "The user id for a new user should be None")
            user.save()
            self.assertIsNotNone(user.id, "After a save the user id should have a generated id")

        for user in self.users:
            if user.id is not None:
                user.delete()


    # def test_hash(self):
    #     crypt = Bcrypt()
    #     users = User.objects.all()
    #     for user in users:
    #         hash =







