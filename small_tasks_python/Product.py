class Product:
    def __init__(self, product_type, price):
        self.product = product_type
        self.price = price

    def sale(self, *name_price_weight):  #makes the arguments a tuple
        return name_price_weight

        

