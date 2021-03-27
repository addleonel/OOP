class Account:
    __id: int
    __name: str
    __document: str
    __email: str
    __password: str

    def __init__(self, id: int, name: str, document: str, 
                email: str = None, password: str = None):
        self.__id = id
        self.__name = name 
        self.__document = document
        self.__email = email
        self.__password = password
    
    @property
    def get_name(self):
        return self.__name
    
    @get_name.setter
    def set_name(self, value):
        self.__name = value
    
    @property
    def get_document(self):
        return self.__document
    
    @get_document.setter
    def set_document(self, value):
        self.__document = value

    @property
    def get_email(self):
        return self.__email
    
    @get_email.setter
    def set_email(self, value):
        self.__email = value
    
    @property
    def get_password(self):
        return self.__password
    
    @get_password.setter
    def set_password(self, value):
        self.__password = value