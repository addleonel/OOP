from car import Car
from account import Account 

class UberPool(Car):

    brand: str
    model: str

    def __init__(self, id: int, license: str, driver: Account, passengers: int, brand: str, model: str):
        super(UberPool, self).__init__(id, license, driver, passengers)
        self.brand = brand
        self.model = model

    def print_data(self):
        print(f'Id: {self.id}, License: {self.license}, Driver: {self.driver.name},\
            Passengers: {self.passengers}, Brand: {self.brand}, Model: {self.model}')