import re
# count=0
x="[0-9]"
matcher=re.finditer(x,"abngt# hrcDF565hh87vf23arfcba")
for match in matcher:
    print(match.start())
    print(match.group())
#     count+=1


# print("count",count)
import re
# count=0
x="[^a-zA-Z0-9]"
matcher=re.finditer(x,"abngt# hrcakbdc@arfcba")
for match in matcher:
    print(match.start())
    print(match.group())
#     count+=1
# print("count",count)

