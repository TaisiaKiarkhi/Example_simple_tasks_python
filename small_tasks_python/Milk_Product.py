from Product import Product
class Milk_Product(Product): #inheritance

	def __init__(self, type_of_milk, if_lactose, type_of_product):
		self.type_of_milk = type_of_milk
		self.lactose = if_lactose
		self.type_of_product = type_of_product

	def sale(self, *name_price_weight): #override
		initial_info = (self.lactose, self.type_of_milk, self.type_of_product)
		merge = initial_info + name_price_weight
		return merge
	
	def lactose_warning(self, if_lactose):
		if if_lactose:
			print("This product contains lactose")
		



