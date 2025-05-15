#!/usr/bin/env python3

# define the class
class CashRegister:
  def __init__(self,discount=0):
      self.discount = discount
      self.total = 0
      self.items =[]
      self.last_transaction = 0


# add items
  def add_item(self,title,price,quantity=1):
        self.total += price * quantity
        self.last_transaction = price * quantity
        for _ in range(quantity):
            self.items.append(title)

  
      # Apply discount
  def apply_discount(self):
           if self.discount > 0:
            discount_amount = self.total * (self.discount / 100.0)
            self.total -= discount_amount
            print (f"After the discount, the total comes to ${int(self.total)}.")
           else:
            print ("There is no discount to apply.")

    # get items
  def get_items(self):
          return self.items
      
      # void last transaction
  def void_last_transaction(self):
         self.total -= self.last_transaction
         self.last_transaction = 0
