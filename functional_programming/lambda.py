#lambda
#to reduce code

def cube(x):
    print(x**3)
cube(5)

#using lamda function

cube=lambda n:n**3
print(cube(6))

add=lambda x,y:x+y
print(add(5,4))

#hello..h
#world..w
#to print first letter

w=lambda string:string[0]
print(w("hello"))
print(w("arya"))
