# import re
#
# x="\w"
# matcher=re.finditer(x,"at# SD@#$ ")
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x="\W"
# matcher=re.finditer(x,"at# SD@#$ ")
# for match in matcher:
#     print(match.start())
#     print(match.group()

# import re
# x="\d"
# matcher=re.finditer(x,"a2t# SD3@#$5 ")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
# import re
# x="\D"
# matcher=re.finditer(x,"a2t# SD3@#$5 ")
# for match in matcher:
#     print(match.start())
#     print(match.group())


import re
x="\s"   #space check
matcher=re.finditer(x,"a2t# SD3@#$5 ")
for match in matcher:
    print(match.start())
    print(match.group())
