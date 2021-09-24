#...inheritance...the properties of one class is given to another classs
#below is examole of ""single inheritance""
class Person:      #this class id called base class/parent class/super class
    def walk(self):
        print("person is walking")
    def read(self):
        print("person is reading")
class Student(Person):  #here person class is inherited in student class is called(child class/sub class/derived class
    def exam(self):
        print("student attending exam")
pe=Person()
pe.walk()
pe.read()
stu=Student()
stu.exam()
stu.walk()
stu.read()
