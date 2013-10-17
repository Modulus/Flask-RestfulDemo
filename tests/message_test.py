from models.user import User

__author__ = 'Modulus'


from models.message import Message

from unittest import TestCase


class MessageTest(TestCase):

    def setUp(self):
        self.message = Message()
        self.users = User.objects

    def tearDown(self):
        self.message.delete()

    def test_save(self):
        self.message.subject = "First message"
        self.message.text = "This is the first message ever in the system"
        self.message.receiver = self.users[1]
        self.assertIsNone(self.message.id)
        self.message.save()
        self.assertIsNotNone(self.message.id)



