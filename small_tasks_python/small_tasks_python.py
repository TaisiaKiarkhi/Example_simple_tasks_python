from functions import calc_age

print("Hello! Welcome to this little program. Enter your age: ")

age = int(input())

if(age<0):
    age_valid = False
    while not(age_valid):
        age = int(input("The age is not valid. Please, try again: "))
        if(age>0):
            age_valid = True

print("Your age in days is " + str(calc_age(age)))






