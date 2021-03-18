class Account:
    id: int
    name: str
    document: str
    email: str = None
    password: str = None

    def __init__(self, id: int, name: str, document: str):
        self.id = id
        self.name = name 
        self.document = document

if __name__ == '__main__':
    print("hello")