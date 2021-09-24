class Person:
    def setvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child(Person):
    def setv(self,std,div):
        self.std=std
        self.div=div
        print(self.std,self.div)
class Student(Child):
    def set(self,marks):
        self.marks=marks
        print(self.marks)
stu=Student()
stu.setvalue("arya",22)
stu.setv(10,"A")
stu.set(100)
