from payment import Payment

class Paypal(Payment):
    email: str
    
    def __init__(self, id: int, email: str):
        super(Paypal, self).__init__(id)
        self.email = email