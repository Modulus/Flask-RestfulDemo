from models.user import User

__author__ = 'Modulus'

from models.message import Message
from resources.testdata.populator import Populator

from unittest import TestCase


class MessageTest(TestCase):

    def setUp(self):
        self.pop = Populator()
        self.pop.run()

        self.message = Message()
        self.users = User.objects

    def tearDown(self):
        if self.message.id is not None:
            self.message.delete()
        self.pop.clear()

    def test_save(self):
        self.message.subject = "First message"
        self.message.text = "This is the first message ever in the system"
        self.message.receiver = self.users[1]
        self.message.sender = self.users[0]
        self.assertIsNone(self.message.id)
        self.message.save()
        self.assertIsNotNone(self.message.id)



