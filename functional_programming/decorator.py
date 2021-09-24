#div

def revert_val(func):
    def wrapper(no1,no2):
        if no1<no2:
            (no1,no2)=(no2,no1)
            return func(no1,no2)
        else:
            return func(no1,no2)
    return wrapper

@revert_val
def div(no1,no2):
    return(no1/no2)
print(div(2,10))

# sub
def revert_val(func):
     def wrapper(num1,num2):
         if num1<num2:
             (num1,num2)=(num2,num1)
             return func(num1,num2)
         else:
             return func(num1,num2)
     return wrapper

@revert_val
def sub(num1,num2):
    return(num1-num2)
print(sub(2,10))
