# Exercise 5.8 Card payments

## "Dumb" payment card

In a previous part we created a class called PaymentCard. The card had methods for eating affordably and heartily, and also for adding money to the card.

However, there was a problem with the PaymentCard class that is implemented in this fashion. The card knew the prices of the different lunches, and therefore was able to decrease the balance by the proper amount. What about if the prices are raised? Or new items are added to the list of offered products? A change in the pricing would mean that all the existing cards would have to be replaced with new cards that are aware of the new prices.

An improved solution is to make the cards "dumb" unaware of the prices and products that are sold, and only keeping track of their balance. All the intelligence is better placed in separate objects, payment terminals.

Let's first implement the "dumb" version of the PaymentCard. The card only has methods for asking for the balance, adding money, and taking money. Complete the method `def take_money(self, amount)` in the class below (and found in the exercise template), using the following as a guide:

```python
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
```

Test main program:

```python
def main():
    petesCard = PaymentCard(10)

    print("money " + str(petesCard.balance)
    was_successful = petesCard.take_money(8)
    print("successfully withdrew: " + str(was_successful))
    print("money " + str(petesCard.balance)

    was_successful = petesCard.take_money(4)
    print("successfully withdrew: " + str(was_successful))
    print("money " + str(petesCard.balance)
}
```

The output should be like below

```plaintext
money 10.0
successfully took: true
money 2.0
successfully took: false
money 2.0
```

## Payment terminal and cash

When visiting a student cafeteria, the customer pays either with cash or with a payment card. The cashier uses a payment terminal to charge the card or to process the cash payment. First, let's create a terminal that's suitable for cash payments.

The outline of the payment terminal. The comments inside the methods tell the wanted functionality:

```python
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
```

The terminal starts with 1000 pounds in it. Implement the methods so they work correctly, using the basis above and the example prints of the main program below.

```python
def main():
    exact_amount = PaymentTerminal()

    change = exact_amount.eat_affordably(10)
    print("remaining change " + str(change))

    exact_amount.eat_affordably(5)
    print("remaining change " + str(change))

    exact_amount.eat_heartily(4.3)
    print("remaining change " + str(change))

    print(exact_amount)
```

```plaintext
remaining change: 7.5
remaining change: 2.5
remaining change: 0.0
money: 1009.3, number of sold afforable meals: 2, number of sold hearty meals: 1
```

## Card payments

Let's extend our payment terminal to also support card payments. We are going to create new methods for the terminal. It receives a payment card as a parameter, and decreases its balance by the price of the meal that was purchased. Here are the outlines for the methods, and instructions for completing them.

```python
class PaymentTerminal:
    # ...

    def eat_affordably(self, card):
        # an affordable meal costs 2.50 pounds
        # if the payment card has enough money, the balance of the card is decreased by the price, and the method returns true
        # otherwise false is returned

    def eat_heartily(self, card):
        # a hearty meal costs 4.30 pounds
        # if the payment card has enough money, the balance of the card is decreased by the price, and the method returns true
        # otherwise false is returned

    # ...
```

**NB:** card payments don't increase the amount of cash in the register.

**Hint:** Try using a `if type(payment) == float or type(payment) == int:` statement to work out whether the customer pays by card or cash. Handle each case differently.

Below is a main program to test the classes, and the output that is desired:

```python
def main():
    exact_amount = PaymentTerminal()

    change = exact_amount.eat_affordably(10)
    print("remaining change: " + str(change))

    annes_card = PaymentCard(7)

    was_successful = exact_amount.eat_heartily(annes_card)
    print("there was enough money: " + str(was_successful))
    was_successful = exact_amount.eat_heartily(annes_card)
    print("there was enough money: " + str(was_successful))
    was_successful = exact_amount.eat_affordably(annes_card)
    print("there was enough money: " + str(was_successful))

    print(exact_amount)
```

```plaintext
remaining change: 7.5
there was enough money: true
there was enough money: false
there was enough money: true
money: 1002.5, number of sold afforable meals: 2, number of sold hearty meals: 1
```

## Adding money

Let's create a method for the terminal that can be used to add money to a payment card. Recall that the payment that is received when adding money to the card is stored in the register. The basis for the method:

```python
def add_money_to_card(self, card, sum):
    # ...
```

A main program to illustrate:

```python
def main():
    exact_amount = PaymentTerminal()
    print(exact_amount)

    annes_card = PaymentCard(2)

    print("amount of money on the card is " + str(annes_card.balance) + " pounds")

    was_successful = exact_amount.eat_heartily(annes_card)
    print("there was enough money: " + str(was_successful))

    exact_amount.add_money_to_card(annes_card, 100)

    was_successful = exact_amount.eat_heartily(annes_card)
    print("there was enough money: " + str(was_successful))

    print("amount of money on the card is " + str(annes_card.balance) + " pounds")

    print(exact_amount)
```

```plaintext
money: 1000.0, number of sold afforable meals: 0, number of sold hearty meals: 0
amount of money on the card is 2.0 pounds
there was enough money: false
there was enough money: true
amount of money on the card is 97.7 pounds
money: 1100.0, number of sold afforable meals: 0, number of sold hearty meals: 1
```
