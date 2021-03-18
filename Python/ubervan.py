from car import Car
from account import Account

class UberVan(Car):
    type_car_accepted: list
    seats_materials: list

    def __init__(self, id: int, license: str, driver: Account, passengers: int, type_car_accepted: list, seats_materials: list):
        super(UberVan, self).__init__(id, license, driver, passengers)
        self.type_car_accepted = type_car_accepted
        self.seats_materials = seats_materials
    
    def print_data(self):
        print(f'Id: {self.id}, License: {self.license}, Driver: {self.driver.name}, Passengers: {self.passengers}')