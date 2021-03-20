from payment import Payment

class Card(Payment):
    number: int
    cvv: str
    date: str

    def __init__(self, id: int, number: int, cvv: str, date: str):
        super(Card, self).__init__(id)
        self.number = number
        self.cvv = cvv
        self.date = date 