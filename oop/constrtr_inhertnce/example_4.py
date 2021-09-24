class Student:
    college="vast"
    def __init__(self,name,roll_no,department):
        self.name=name
        self.roll_no=roll_no
        self.department=department
    def printvalue(self):
        print(self.name)
        print(self.roll_no)
        print(self.department)
        print(Student.college)
    def __str__(self):
        return self.name + str(self.roll_no)

stu=Student("arya",30,"ECE")
stu.printvalue()
print(stu)