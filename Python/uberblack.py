from car import Car
from driver import Driver

class UberBlack(Car):
    
    __type_car_accepted: list
    __seats_materials: list

    def __init__(self, id: int, license: str, driver: Driver, type_car_accepted: list, seats_materials: list):
        super(UberBlack, self).__init__(id, license, driver)
        self.__type_car_accepted = type_car_accepted
        self.__seats_materials = seats_materials 
    
    def print_data(self):
        super(UberBlack, self).print_data()
        print(f'Type car accepted: {self.__type_car_accepted}, Seat materials: {self.__seats_materials}')
    
    @property
    def get_uberblack_passengers(self):
        return self.get_password
    
    @get_uberblack_passengers.setter
    def set_uberblack_passengers(self, value):
        assert value <= 6, 'It should be 6 or lower than 6'
        self.set_passengers = value

    @property
    def get_type_car_accepted(self):
        return self.__type_car_accepted
    
    @get_type_car_accepted.setter
    def set_type_car_accepter(self, value):
        self.__type_car_accepted = value

    @property
    def get_seats_materials(self):
        return self.__seats_materials
    
    @get_seats_materials.setter
    def set_seats_materials(self, value):
        self.__seats_materials = value