from itertools import product
A=[i for i in map(int,raw_input().split())]
B=[i for i in map(int,raw_input().split())]
A.sort()
B.sort()
print A
print B

list2= list((x,y) for x in A for y in B)
for i in list2:
    print i,

