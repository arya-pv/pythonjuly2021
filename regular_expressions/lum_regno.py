import re
f2=open("validreg","w")
f1=open("lum_regno","r")
x='[L][U][M][0-9]{2}[P][Y][0-9]{3}$'
for num in f1:
    number=num.rstrip("\n")  #to strio(\n)...to read line by line
    matcher = re.fullmatch(x,number)
    if matcher is not None:
        f2.write(number)
        f2.write("\n")