import pytest
import os

def test_exercise():
    os.chdir('src')

    from payment_card import PaymentCard
    from payment_terminal import PaymentTerminal
    card = PaymentCard(10)

    assert card.balance == 10

    assert card.take_money(8)
    assert not card.take_money(4)

    amount = PaymentTerminal()
    assert amount.eat_affordably(10) == 7.5

    amount = PaymentTerminal()
    change = amount.eat_affordably(10)

    card = PaymentCard(7)

    assert amount.eat_heartily(card)
    assert not amount.eat_heartily(card)
    assert amount.eat_affordably(card)

    amount = PaymentTerminal()
    card = PaymentCard(2)

    assert card.balance == 2

    assert not amount.eat_heartily(card)

    amount.add_money_to_card(card, 100)

    assert amount.eat_heartily(card)

    assert card.balance == 97.7
