from functions import calc_age
from Worker import Worker
print("Hello! Welcome to this little program. Enter your age: ")

age = int(input())


if(age<0):
    age_valid = False
    while not(age_valid):
        age = int(input("The age is not valid. Please, try again: "))
        if(age>0):
            age_valid = True

print("Your age in days is " + str(calc_age(age)))

worker_1 = Worker("Alex Table", age, "Clerk")

print(worker_1.name)

for i in range (0, 12):
    worker_1.add_salary(int(input()))
    print(worker_1.monthly_salary[i])

print(worker_1.monthly_salary)




