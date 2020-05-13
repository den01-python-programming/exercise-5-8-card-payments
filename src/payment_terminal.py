class PaymentTerminal:

    def __init__(self):
        self.money = 0 # amount of cash
        self.affordable_meals = 0 # number of sold affordable meals
        self.hearty_meals = 0 # number of sold hearty meals

    def eat_affordably(self,payment):
        # an affordable meal costs 2.50 pounds
        # increase the amount of cash by the price of an affordable mean and return the change
        # if the payment parameter is not large enough, no meal is sold and the method should return the whole payment

    def eat_heartily(self,payment):
        # a hearty meal costs 4.30 pounds
        # increase the amount of cash by the price of a hearty mean and return the change
        # if the payment parameter is not large enough, no meal is sold and the method should return the whole payment

    def __str__(self):
        return "money: " + str(self.money) + ", number of sold afforable meals: " + str(self.affordable_meals) + ", number of sold hearty meals: " + str(self.hearty_meals)
