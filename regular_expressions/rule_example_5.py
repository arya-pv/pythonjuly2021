#last position must be a number

import re
n=input("enter number to valid")
x="[a-zA-Z]+\d$"
matcher=re.fullmatch(x,n)
if matcher is not None:
    print("valid")
else:
    print("invalid")

#minimumlenght8 and maxi lenght 15 and except numbers

import re
n=input("enter word")
x='([\D]{8,15})'
matcher=re.fullmatch(x,n)
if matcher is not None:
    print("valid")
else:
    print("invalid")
