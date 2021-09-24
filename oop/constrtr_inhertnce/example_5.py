class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name)
        print(self.age)
class Teacher(Parent):
    def __init__(self,school,department,name,age):
        super().__init__(name,age)
        self.school=school
        self.department=department
    def print(self):
        print(self.school)
        print(self.department)
    def __str__(self):
        return self.school + self.name

obj=Teacher("vidya","ece","anu",25)
obj.print()
obj.printval()
print(obj)