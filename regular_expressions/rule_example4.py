#vehicle registration number

import re
n=input("enter vehicle number to validate")
x="[K][L]\d{2}[A-Z]{2}\d{4}"
matcher=re.fullmatch(x,n)
if matcher is not None:
    print("valid")
else:
    print("invalid")

#starting with upper case
# then numbers lower case,symbols

import re
n=input("enter")
x='[A-Z][a-z0-9\W]*'
matcher=re.fullmatch(x,n)
if matcher is not None:
    print("valid")
else:
    print("invalid")