from itertools import combinations
A=map(int,raw_input().split())
C=list(combinations(A,4))
d=[]
for i in C:
    e=0
    for k in i:
        e=e+k
    d.append(e)

d.sort()
print d[0],d.pop()

