from car import Car
from driver import Driver

class UberX(Car):

    brand: str
    model: str
    
    def __init__(self, id: int, license: str, driver: Driver, brand: str, model: str):
        super(UberX, self).__init__(id, license, driver)
        self.brand = brand
        self.model = model

    def print_data(self):
        super(UberX, self).print_data()
        print(f'Brand: {self.brand}, Model: {self.model}')
    
    @property
    def uberx_passengers(self):
        return self.passengers 
    
    @uberx_passengers.setter
    def uberx_passengers(self, value):
        assert value <= 3, 'It should be 3 or lower than 3'
        self.passengers = value