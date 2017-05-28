import math
T=int(input())
c=[]
for i in range(0,T):
    A,B=map(int,raw_input().split())
    c.append([A,B])
x=[]
for i in range(0,T):
    d=int(math.floor(math.sqrt(c[i][1]))-math.floor(math.sqrt(c[i][0])))
    if math.sqrt(c[i][0])==math.floor(math.sqrt(c[i][0])):
        x.append(d+1)
    else:
        x.append(d)

for i in x:
    print i
