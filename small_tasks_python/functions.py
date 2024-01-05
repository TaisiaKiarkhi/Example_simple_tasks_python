def calc_age(age):
    days = age * 365
    return days

mutliply = lambda x, y : x*y
devision = lambda x,y: x/y
power = lambda x,y: x ** y

def products_dict(meat_, fish_, **new_category):
        merged = {**meat_, **fish_, **new_category}
        return merged
