#coding: utf-8
from models.message import Message
from models.user import User
from datetime import datetime

__author__ = 'Modulus'


class Populator(object):

    def clear(self):
        User.drop_collection()
        Message.drop_collection()

    def run(self):

        User.drop_collection()
        Message.drop_collection()

        user1 = User()
        user2 = User()
        user3 = User()
        user4 = User()

        user1.firstName = "John"
        user1.lastName = "Doe"
        user1.birthDate = datetime.now()
        user1.userName = "Creator"
        user1.passHash = user1.userName

        user2.firstName = "Jane"
        user2.lastName = "Doe"
        user2.birthDate = datetime.now()
        user2.userName = "Nemesis"
        user2.passHash = user2.userName

        user3.firstName = "Michelle"
        user3.lastName = "Nielsen"
        user3.birthDate = datetime.now()
        user3.userName = "GoldDigger86"
        user3.passHash = user3.userName

        user4.firstName = "Leif"
        user4.lastName = "Paulsen"
        user4.birthDate = datetime.now()
        user4.userName = "The_Artist"
        user4.passHash = user4.userName

        user1.save()
        user2.save()
        user3.save()
        user4.save()

        message1 = Message()
        message1.subject = "First message"
        message1.text = "This is the first message ever in the system. Hello Jane this is John, how are you?"
        message1.sender = user1
        message1.receiver = user2
        message1.save()

        message2 = Message()
        message2.subject = "Second message"
        message2.text = "This is the second message ever in the system. Hello Jane this is Åge, how are you?"
        message2.sender = user4
        message2.receiver = user2
        message2.save()

        message3 = Message()
        message3.subject = "Second message"
        message3.text = "This is the Third message ever in the system. Hello Jane this is Åge, how are you?"
        message3.sender = user4
        message3.receiver = user1
        message3.save()

if __name__ == "__main__":

    pop = Populator()
    pop.run()
