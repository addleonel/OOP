from payment import Payment

class Cash(Payment):
    def __init__(self, id: int):
        super(Cash, self).__init__(id)