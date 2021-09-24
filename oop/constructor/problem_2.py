class Teacher:
    school="vidya"
    def __init__(self,name,id,department,subject):
        self.name=name
        self.id=id
        self.department=department
        self.subject=subject
    def printvalue(self):
        print(self.name)
        print(self.id)
        print(self.department)
        print(self.subject)
        print(Teacher.school)
te=Teacher("anu",302,"ec","maths")
te.printvalue()
te1=Teacher("arya",303,"eee","hindi")
te1.printvalue()

