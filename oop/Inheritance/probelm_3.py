#multiple inheritance

class Person:
    def set(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Parent:
    def setv(self,adrs,job):
        self.adrs=adrs
        self.job=job
        print(self.adrs,self.job)
class Employee(Person,Parent):
    def setvalue(self,role,salary):
        self.role=role
        self.salary=salary
        print(self.role,self.salary)
em=Employee()
em.set("arya",25)
em.setv("paramel","IT")
em.setvalue("developr",30000)