import re
f1=open("phn_num","r")
x='[+][9][1]\d{10}$'
for num in f1:
    number=num.rstrip("\n")  #to strio(\n)...to read line by line
    matcher = re.fullmatch(x,number)
    if matcher is not None:
        print(number)