class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print("name",self.name)
        print("age",self.age)
class Employee(Person):
    def __init__(self,company,salary,name,age):
        super().__init__(name,age)
        self.company=company
        self.salary=salary
    def printval(self):
        print("company name",self.company)
        print("salary",self.salary)

obj=Employee("TCS",10000,"arya",24)
obj.print()
obj.printval()