class PaymentCard:

    def __init__(self, balance):
        self.balance = balance

    def balance(self):
        return self.balance

    def add_money(self, increase):
        self.balance = self.balance + increase

    def take_money(self, amount):
        # implement the method so that it only takes money from the card if
        # the balance is at least the amount parameter.
        # returns true if successful and false otherwise
