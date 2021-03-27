from car import Car
from driver import Driver 

class UberPool(Car):

    __brand: str
    __model: str

    def __init__(self, id: int, license: str, driver: Driver, brand: str, model: str):
        super(UberPool, self).__init__(id, license, driver)
        self.__brand = brand
        self.__model = model

    def print_data(self):
        super(UberPool, self).print_data()
        print(f'Brand: {self.__brand}, Model: {self.__model}')
    
    @property
    def get_uberpool_passengers(self):
        return self.get_passengers 
    
    @get_uberpool_passengers.setter
    def set_uberpool_passengers(self, value):
        assert value <= 4, 'It should be 4 or lower than 4'
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