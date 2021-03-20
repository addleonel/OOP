from account import Account

class User(Account):
    def __init__(self, id: int, name: str, document: str):
        super(User, self).__init__(id, name, document)