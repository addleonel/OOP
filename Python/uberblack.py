from car import Car
from driver import Driver

class UberBlack(Car):
    
    type_car_accepted: list
    seats_materials: list

    def __init__(self, id: int, license: str, driver: Driver, type_car_accepted: list, seats_materials: list):
        super(UberBlack, self).__init__(id, license, driver)
        self.type_car_accepted = type_car_accepted
        self.seats_materials = seats_materials 
    
    def print_data(self):
        super(UberBlack, self).print_data()
        print(f'Id: {self.id}, License: {self.license}, Driver: {self.driver.name}, Passengers: {self.passengers}')