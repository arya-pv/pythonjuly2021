import re
n='56kg'
x='[0-9]{2}[a-z]{2}'
matcher=re.fullmatch(x,n)
if matcher is not None:
    print("valid")
else:
    print("invalid")
