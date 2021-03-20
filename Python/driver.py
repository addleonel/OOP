from account import Account

class Driver(Account):
    def __init__(self, id: int, name: str, document: str):
        super(Driver, self).__init__(id, name, document)