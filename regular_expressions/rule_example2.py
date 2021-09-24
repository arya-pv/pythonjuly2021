import re

n=input("enter the num to validate")
x="\d{10}"
matcher=re.fullmatch(x,n)
if matcher is not None:
    print("valid")
else:
    print("invalid")


#indian numbers validate
import re
n=input("enter the num to validate")
x="[+][9][1]\d{10}"
matcher=re.fullmatch(x,n)
if matcher is not None:
    print("valid")
else:
    print("invalid")