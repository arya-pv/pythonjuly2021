import re
#
x="a+"
r="aaa abc dfa asda"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
#

# import re
#
# x = "a*"
# r = "aaa abc dfa asda"
# matcher = re.finditer(x, r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x = "a?"
# r = "aaa abc dfa asd"
# matcher = re.finditer(x, r)
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
#
# x = "a{2}"
# r = "aaa abc dfa aasda"
# matcher = re.finditer(x, r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#
# import re
#
# x = "a{1,3}"
# r = "aaa abc dfa aasda"
# matcher = re.finditer(x, r)
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
#
# x = "^a"
# r = "aaa abc dfa aasda"
# matcher = re.finditer(x, r)
# for match in matcher:
#      print(match.start())
#      print(match.group())

#
# import re
#
# x = "a$"
# r = "aaa abc dfa aasda"
# matcher = re.finditer(x, r)
# for match in matcher:
#      print(match.start())
#      print(match.group())