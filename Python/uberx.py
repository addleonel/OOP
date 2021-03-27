from car import Car
from driver import Driver

class UberX(Car):

    __brand: str
    __model: str
    
    def __init__(self, id: int, license: str, driver: Driver, brand: str, model: str):
        super(UberX, self).__init__(id, license, driver)
        self.__brand = brand
        self.__model = model

    def print_data(self):
        super(UberX, self).print_data()
        print(f'Brand: {self.__brand}, Model: {self.__model}')
    
    @property
    def get_uberx_passengers(self):
        return self.get_passengers 
    
    @get_uberx_passengers.setter
    def set_uberx_passengers(self, value):
        assert value <= 3, 'It should be 3 or lower than 3'
        self.set_passengers = value
    
    @property
    def get_brand(self):
        return self.__brand
    
    @get_brand.setter
    def set_brand(self, value):
        self.__brand = value

    @property
    def get_model(self):
        return self.__model
    
    @get_model.setter
    def set_model(self, value):
        self.__model = value