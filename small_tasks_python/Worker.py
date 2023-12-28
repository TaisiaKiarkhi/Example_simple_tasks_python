
class Worker:
    

    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
        self.monthly_salary = []
    
    def add_salary(self, salary):
        if  not self.monthly_salary:
                self.monthly_salary.append(salary)
        else:
            self.monthly_salary.append(salary)
    
    #average per month in a year
    def average_salary():
        sum_ = 0
        for money in self.monthly_salary:
            sum_ = sum_ + money
        total = sum_/12
        return total

