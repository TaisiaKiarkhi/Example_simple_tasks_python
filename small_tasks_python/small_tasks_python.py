from functions import calc_age
from Worker import Worker
from information import input_info, dict_positions, sort_positions
from Customer import Customer
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

print(worker_1.name)

for i in range (0, 3):
    worker_1.add_salary(int(input()))
    #print(worker_1.monthly_salary[i])

print(worker_1.monthly_salary)
print(str(worker_1.average_salary()))

input_info()
sort_positions()
print("To find people who work as clerks type Clerk, to find people who works as managers type Manager")
print(dict_positions[str(input())])

