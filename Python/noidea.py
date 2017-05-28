n,m=map(int,raw_input().split())

D=map(int,raw_input().split())

A=map(int,raw_input().split())
B=map(int,raw_input().split())
c=0
for i in A:
    for k in D:
        if i==k:
            c=c+1
d=0
for p in B:
    for l in D:
        if p==l:
            d=d+1


print(c-d)
