class Person:
    def set(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Employee(Person):
    def set(self,salary,jobrole):
        self.salary=salary
        self.jobrole=jobrole
        print(self.salary,self.jobrole)
obj=Employee()
obj.set("ANU",23,3000,"HR")

class Operators:
    def num(self,num1):
        self.num1=num1
        print(self.num1)
    def num(self,num2,num3):
        self.num2=num2
        self.num3=num3
        print(num2+num3)
obj=Operators()
obj.num(3)

