#constructoe is used to initialize instance variable

class Person:
    def __init__(self,name,age,address):   #__init__ it is the constructor
        self.name=name
        self.age=age
        self.address=address
    def printvalue(self):
        print(self.name,self.age,self.address)

obj=Person("anu",23,"paramel house")  #by using constructor we put the things inside the object itself
obj.printvalue()
