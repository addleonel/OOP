
from car import Car
from account import Account
from uberx import UberX
from uberpool import UberPool

if __name__ == '__main__':
    thomas = Account(1, 'Thomas', '23456789')
    leonel = Account(2, 'Leonel', '12344556')
    
    thomas_car = Car(1, 'T-800', thomas)
    my_car = Car(2, 'MD455', leonel)

    # Without passengers
    thomas_car.print_data()
    my_car.print_data()

    # With passengers
    thomas_car.passengers = 4
    my_car.passengers = 5

    thomas_car.print_data()
    my_car.print_data()

    print('-'*40)

    thomas_uberx = UberX(1, 'FTM45', thomas, 'Chevrolet', 'Blazer')
    my_uberx = UberX(2, 'LMV-NT', leonel, 'Toyota', 'Avalon')

    thomas_uberx.print_data()
    my_uberx.print_data()

    thomas_uberx.uberx_passengers = 3
    thomas_uberx.print_data()

    # thomas_uber_pool = UberPool(1, 'FTM45', thomas, 2, 'Ferrari', 'Roma')
    # my_uber_pool = UberPool(2, 'LMV-NT', leonel, 3, 'Ford', 'Aspire')

    # thomas_uber_pool.print_data()
    # my_uber_pool.print_data()