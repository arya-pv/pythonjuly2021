class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b


a = int(input("enter first number"))
b = int(input("enter second number"))
obj = Calculator(a, b)
obj.add()
print(obj.sub())
print(obj.mul())
