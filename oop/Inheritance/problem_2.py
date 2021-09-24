#multiple inheritance

class Person:
    def set(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child:
    def setv(self,std,school):
        self.std=std
        self.school=school
        print(self.std,self.school)
class Student(Person,Child):
    def setvalue(self,roll_no,marks):
        self.roll_no=roll_no
        self.marks=marks
        print(self.roll_no,self.marks)

stu=Student()
stu.set("arya",15)
stu.setv(10,"infant jesus")
stu.setvalue(28,100)

#student class parent classses are person class and child