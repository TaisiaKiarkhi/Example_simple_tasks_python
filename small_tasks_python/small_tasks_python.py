from itertools import product
from functions import calc_age, products_dict
from Worker import Worker
from information import input_info, dict_positions, sort_positions
from Customer import Customer
from Product import Product
from Milk_Product import Milk_Product
print("Hello! Welcome to this little program. Enter your age: ")

age = int(input())


if(age<0):
    age_valid = False
    while not(age_valid):
        age = int(input("The age is not valid. Please, try again: "))
        if(age>0):
            age_valid = True

print("Your age in days is " + str(calc_age(age)))

#worker_1 = Worker("Alex Table", age, "Clerk")
worker_1 = Worker(age = age, name = "Alex Table", position= "Clerk")
customer1 = Customer("John Jack", age = 32)
customer1.check_age()

#print(worker_1.name)
#
#for i in range (0, 3):
#    worker_1.add_salary(int(input()))
#    #print(worker_1.monthly_salary[i])
#
#print(worker_1.monthly_salary)
#print(str(worker_1.average_salary()))
#
#input_info()
#sort_positions()
#print("To find people who work as clerks type Clerk, to find people who works as managers type Manager")
#print(dict_positions[str(input())])


bought_items = 0

products = []

bought_items = int(input("Write amount of products you want to buy"))

for i in range(0, bought_items):
    name = str(input("Type the name of the product: "))
    price = float(input("Type the price of the product: "))
    
    products.append(Product(name, price))



if bought_items>=2 : #20% discount
    discount = lambda total_price: total_price * 0.8
    total = 0
    for i in range(0, len(products)):
        total = total + products[i].price
    print(discount(total))

repeat_products = products * 10 #repeats each element 10 times
for i in range (0, len(repeat_products)):
     print(repeat_products[i].product)

product_test = Product("Milk", 1.8)

#list_of_products_with_weight = []
#print(product_test.sale(product_test.product, product_test.price, 1000))
#
#for i in range(0,2):
#    list_of_products_with_weight.append(product_test.sale(str(input()), float(input()), float(input())))

meat = {"beef": "Beef meat" "Roast beef" "Meatballs beef", "chicken": "Chicken breast" "Chicken sausages" "Grilled chicken", "pork": "Pork sausages" "Pork meatballs" }
fish = {"salmon": "Salmon fillets" "Nigiri", "tuna": "Canned tuna" "Tuna fillets" }


print(products_dict(meat, fish, milk= "Cow Milk" "Oatmilk", cheese= "Mozzarella" "Feta"))

cheese = Milk_Product("cow_milk", True, "cheese")
print(cheese.sale("Norvegia", 9.1, 700))