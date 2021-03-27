from car import Car
from driver import Driver

class UberVan(Car):
    __type_car_accepted: list
    __seat_materials: list

    def __init__(self, id: int, license: str, driver: Driver, type_car_accepted: list, seat_materials: list):
        super(UberVan, self).__init__(id, license, driver)
        self.__type_car_accepted = type_car_accepted
        self.__seat_materials = seat_materials
    
    def print_data(self):
        super(UberVan, self).print_data()
        print(f'Type car accepted: {self.__type_car_accepted}, Seats materials: {self.__seat_materials}')

    @property
    def get_ubervan_passengers(self):
        return self.get_password
    
    @get_ubervan_passengers.setter
    def set_ubervan_passengers(self, value):
        assert value <= 7, 'It should be 7 or lower than 7'
        self.set_passengers = value

    @property
    def get_type_car_accepted(self):
        return self.__type_car_accepted
    
    @get_type_car_accepted.setter
    def set_type_car_accepter(self, value):
        self.__type_car_accepted = value

    @property
    def get_seat_materials(self):
        return self.__seat_materials
    
    @get_seat_materials.setter
    def set_seat_materials(self, value):
        self.__seat_materials = value