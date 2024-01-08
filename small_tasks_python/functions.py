
ID_dict = {}
Information = []

def calc_age(age):
    days = age * 365
    return days

mutliply = lambda x, y : x*y
devision = lambda x,y: x/y
power = lambda x,y: x ** y

def products_dict(meat_, fish_, **new_category):
        merged = {**meat_, **fish_, **new_category}
        return merged

def info(position, company, *personal_info, country, city, ID):
    personal_information = (personal_info)
    work_place = (position, company)
    location = (country, city)
    global Information
    Information.append(personal_information, work_place, location)
    
    global ID_dict
    ID_dict = {ID: Information[-1]}
