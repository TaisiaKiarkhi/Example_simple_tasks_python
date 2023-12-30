age_restriction = 18

class Customer: 
    tax = 0.02   #2 percent
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_age(self):
         global age_restriction
         if self.age< age_restriction:
             print("You are too young")
         else:
             print("You are ok")

    def tax_payment(self, price):
        payment = price * self.tax
        return payment
        