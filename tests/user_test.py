__author__ = 'Modulus'

from models.user import User

from unittest import TestCase


class UserTest(TestCase):

    def setUp(self):
        self.users = [User(), User(), User()]
        for index, user in enumerate(self.users):
            user.firstName = "User_"+str(index)
            user.lastName = "User_"+str(index)+"_lastName"
            user.userName = "UserName_"+str(index)

    def tearDown(self):
        for user in self.users:
            user.delete()

    def test_save(self):
        for user in self.users:
            self.assertIsNone(user.id, "The user id for a new user should be None")
            user.save()
            self.assertIsNotNone(user.id, "After a save the user id should have a generated id")






