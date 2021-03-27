class Router:
    def __init__(self, id: int, start: list, end: list):
        self.__id = id
        self.__start = start
        self.__end = end

    @property
    def get_start(self):
        return self.__start

    @get_start.setter
    def set_start(self, value):
        self.__start = value

    @property
    def get_end(self):
        return self.__end

    @get_end.setter
    def set_end(self, value):
        self.__end = value        