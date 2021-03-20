from driver import Driver


class Car:
    __id: int
    __license: str
    __driver: Driver
    __passengers: int
    
    def __init__(self, id: int, license: str, driver: Driver, passengers: int=None):
        self.__id = id
        self.__license = license
        self.__driver = driver
        self.__passengers = passengers

    def print_data(self):
        message = f'Id: {self.__id}, License: {self.__license}, Driver: {self.__driver.name}, '
        if self.__passengers:
            message += f'Passengers: {self.__passengers}'
        print(message)

    @property
    def passengers(self):
        return self.__passengers
        
    @passengers.setter
    def passengers(self, value):
        assert value >= 0, '\'value\' must not be negative'
        self.__passengers = value
