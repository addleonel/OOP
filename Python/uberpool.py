from car import Car
from driver import Driver 

class UberPool(Car):

    brand: str
    model: str

    def __init__(self, id: int, license: str, driver: Driver, brand: str, model: str):
        super(UberPool, self).__init__(id, license, driver)
        self.brand = brand
        self.model = model

    def print_data(self):
        super(UberPool, self).print_data()
        print(f'Brand: {self.brand}, Model: {self.model}')