# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


def pattern(n):
    for i in range(n):
        num=1
        for j in range(i):
            print(num,end=" ")
            num=num+1
        print()

pattern(5)