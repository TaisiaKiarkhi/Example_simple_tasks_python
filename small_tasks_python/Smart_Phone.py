from Product import Product
from Electronics import Electronics

class Smartphone (Product, Electronics):  #multiple inheritance

	def __init__(price, type_of_product, color):
		super().__init__(type_of_product, price)
		self.__init__(price, "black")


	def turn_on():
		print("Android")
		super().turn_on()

	def turn_off():
		print("Good bye")
		super().turn_off()

