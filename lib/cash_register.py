#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
     formatted_item = f"{title} ${price:.2f}"
     self.total += price * quantity
     self.items.extend([formatted_item] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            self.total *= (100 - self.discount) / 100
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
     if self.items:
        last_item = self.items.pop()
        title, price_str = last_item.rsplit(' $', 1)
        last_price = float(price_str)
        self.total -= last_price
     else:
        print("No transactions to void.")

