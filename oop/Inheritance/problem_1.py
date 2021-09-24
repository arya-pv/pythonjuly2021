class Person:
    def setvalue(self,name,hobby,qualification,):
        self.name=name
        self.hobby=hobby
        self.qualification=qualification
        print(self.name,self.hobby,self.qualification)
class Employee(Person):
    def setvalue(self,company,role,salary):
        self.company=company
        self.role=role
        self.salary=salary
        print(self.company,self.role,self.salary)
em=Employee()
em.setvalue("anu","dance","btech")
em.setvalue("tcs","hr",30000)