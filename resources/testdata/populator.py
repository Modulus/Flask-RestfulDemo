#coding: utf-8
from models.message import Message
from models.user import User
from datetime import datetime

__author__ = 'Modulus'


class Populator(object):

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
        user1.passHash = "No hash"
        user1.userName = "Creator"

        user2.firstName = "Jane"
        user2.lastName = "Doe"
        user2.birthDate = datetime.now()
        user2.passHash = "No hash"
        user2.userName = "Nemesis"

        user3.firstName = "Michelle"
        user3.lastName = "Nielsen"
        user3.birthDate = datetime.now()
        user3.passHash = "No hash"
        user3.userName = "GoldDigger86"

        user4.firstName = "Åge"
        user4.lastName = "Paulsen"
        user4.birthDate = datetime.now()
        user4.passHash = "No hash"
        user4.userName = "The_Artist"

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






if __name__ == "__main__":

    pop = Populator()
    pop.run()
