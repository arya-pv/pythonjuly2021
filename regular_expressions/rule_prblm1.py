import re
# count=0
x="[abc]"
matcher=re.finditer(x,"abngt#hrcakbdcarfcba")
for match in matcher:
    print(match.start())
    print(match.group())
#     count+=1
# print("count",count)