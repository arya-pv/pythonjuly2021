#mail id

import re
n=input("enter your mail id")
x="[a-zA-A0-9]+[@][a-z]+[.][a-z]{2,3}$"
matcher=re.fullmatch(x,n)
if matcher is not None:
    print("valid")
else:
    print("invalid")

#starting with a and ending with b

import re
n=input("enter")
x='^a[a-zA-Z0-9\W]*b$'
matcher=re.fullmatch(x,n)
if matcher is not None:
    print("valid")
else:
    print("invalid")