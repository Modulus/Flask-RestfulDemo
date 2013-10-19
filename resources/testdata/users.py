__author__ = 'Modulus'


class Users():

    def __init__(self):
        self.users = [{"name": "Joe", "id": "1"}, {"name": "Kari", "id": "2"}, {"name":"Cate", "id":"3"},
                      {"name": "Josh", "id":"4"}]

    def get(self):
        return self.users