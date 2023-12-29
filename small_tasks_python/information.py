from Worker import Worker 
worker_list = []

def input_info():
    for i in range(1, 5):
     name = str(input())
     age = int(input())
     position = str(input())
     worker_list.append(Worker(name, age, position))

clerks = [] 
managers = []

def sort_positions():
    for worker in worker_list:
     if worker.position == "Clerk":
         clerks.append(worker.name)
     elif worker.position == "Manager":
         managers.append(worker.name)


dict_positions = {
    "Clerk" : clerks,
    "Manager" : managers
    }

#just to practice 2D-lists
deadlines = [
    ["12.12.2023", "09.10.2023", "28. 11.23"], #for clerks
    ["23.09.2023", "17.11.2023", "19.12. 2023"] #for managers
    ]
 
for row in deadlines:
    for columns in row[0]:
        print(columns)


