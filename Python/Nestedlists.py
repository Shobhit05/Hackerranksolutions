from operator import itemgetter
D=[]
N=int(input())
for i in range(0,N):
    a=raw_input()
    b=float(input())
    D.append([a,b])
E=sorted(D, key=itemgetter(1))
f=E[0][1]

l=[]
for j in range(0,N):
    l.append(E[j][1])

q=l.count(f)
c=E[q][1]
m=l.count(c)
name=[]
print E
print q
print m
for k in range(0,m):
    name.append(E[q][0])
    name.sort()
    q=q+1


for p in name:
    print p


