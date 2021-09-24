lst=[1,2,3,4,5,6,7,8,9,10]
def chk_even(num):
    return num%2==0
evens=list(filter(chk_even,lst))
print(evens)

evens=list(filter(lambda num:num%2==0,lst))
print(evens)

odd_num=list(filter(lambda num:num%2 !=0,lst))
print(odd_num)