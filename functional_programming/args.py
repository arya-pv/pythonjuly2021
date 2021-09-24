#by using star args we can add as many numbers
#star args out is got in tuple
def printvalue(*args):
    return args
print(printvalue(4,5,4,3,45,6,78,0))


def details(**args):
    return args
print(details(name="anu",age=22,place="kochi"))
#to give clarifications to data use **args and out will be in the form dictionar
