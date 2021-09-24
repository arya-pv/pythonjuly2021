class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name",self.name)
        print("age",self.age)
class Student(Person):
    def __init__(self,roll_no,marks,name,age):
        super().__init__(name,age)
        self.roll_no=roll_no
        self.marks=marks
    def printvalue(self):
        print("roll_no",self.roll_no)
        print("marks",self.marks)

cr=Student(2,100,"arya",15)
cr.printval()
cr.printvalue()
