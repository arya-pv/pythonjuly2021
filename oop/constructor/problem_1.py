class Employee:
    def __init__(self,name,id_no,department):
        self.name=name
        self.id_no=id_no
        self.department=department
    def printvalue(self):
        print(self.name,self.id_no,self.department)
obj=Employee("arya",3021,"EC")
obj.printvalue()