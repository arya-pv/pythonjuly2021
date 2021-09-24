class Vehicle:
    def __init__(self,model,no,color):
        self.model=model
        self.no=no
        self.color=color
    def printval(self):
        print("model",self.model)
        print("vehicle no",self.no)
        print("color",self.color)
    def __str__(self):
        return self.model + self.color
obj=Vehicle("dio",3045,"black")
obj.printval()
print(obj)