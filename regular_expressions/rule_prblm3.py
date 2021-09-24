# import re
# count=0
# x="[a-z]"
# matcher=re.finditer(x,"aFGBgt# hrc34nb5670nDF23vfcba")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#     count+=1
# print("count",count)

import re
# count=0
x="[a-zA-Z]"
matcher=re.finditer(x,"aFGBgt# hrc34nb5670nDF23vfcba")
for match in matcher:
    print(match.start())
    print(match.group())
#     count+=1
# print("count",count)