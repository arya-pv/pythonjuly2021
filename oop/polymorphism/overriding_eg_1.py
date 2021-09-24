class Person():
    def set(self,name):
        self.name=name
        print(self.name)
class Employee(Person):
    def set(self,salary):
        self.salary=salary
        print(self.salary)
obj=Employee()
obj.set(4000)