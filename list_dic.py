employees = [
    {"e_id": 1000, "e_name": "ram", "salary": 25000, "department": "testing", "exp": 1},
    {"e_id": 1001, "e_name": "ravi", "salary": 22000, "department": "ba", "exp": 1},
    {"e_id": 1002, "e_name": "raj", "salary": 20000, "department": "mrkt", "exp": 1},
    {"e_id": 1003, "e_name": "nikil", "salary": 26000, "department": "developer", "exp": 1},
    {"e_id": 1004, "e_name": "nivi", "salary": 28000, "department": "developer", "exp": 2},

]
#print employee names only
for employee in employees:
    print(employee["e_name"])

#print employee names in upper case
for employee in employees:
    print(employee["e_name"].upper())

#print employee name who are working as developers

for employee in employees:
    if (employee["department"]=="developer"):
        print(employee["e_name"])

#find total of salaries
total=0
for employee in employees:
    total+=employee["salary"]
print("total salary=",total)



#first case is mappping
#second case is filtering
#third case reduce

#print employee names whos name starting with a

e_names=list(map(lambda employee:employee["e_name"],employees))
print(e_names)

e_upper=list(map(lambda employee:employee["e_name"].upper(),employees))
print(e_upper)

developers=list(filter(lambda employee:employee["department"]=="developer",employees))
print(developers)

developers_name=list(map(lambda developer:developer["e_name"],developers))
print(developers_name)

developers_name=list(map(lambda developer:developer["e_name"],list(filter(lambda employee:employee["department"]=="developer",employees))  ))
print(developers_name)

salary=min(list(map(lambda employee:employee["salary"],employees)))
print(salary)


#reduce is not directly available,we have to import that module

from functools import reduce
