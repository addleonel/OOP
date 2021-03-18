from account import Account

class Car:
    id: int
    license: str
    driver: Account
    passengers: int
    
    def __init__(self, id: int, license: str, driver: Account, passengers: int):
        self.id = id
        self.license = license
        self.driver = driver
        self.passengers = passengers
    
    def print_data(self):
        print(f'Id: {self.id}, License: {self.license}, Driver: {self.driver.name}, Passengers: {self.passengers}')

if __name__ == '__main__':
    print('carhello')