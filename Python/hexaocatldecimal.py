from decimal import Decimal
import string

n=int(input())

A=[str(x) for x in range(1,n+1)]
B=[oct(x) for x in range(1,n+1)]
C=[hex(x) for x in range(1,n+1)]
D=[bin(x) for x in range(1,n+1)]
X=[]
Y=[]
Z=[]
m=[]
for i in A:
    X.append(i)
for i in B:
    Y.append(i[1:])



for i in C:
    Z.append(string.upper(i[2:]))


for i in D:
    m.append(i[2:])

Q=[X,Y,Z,m]


for i in range(0,n):
    c=bin(n)
    d=c[2:]
    e=len(d)
    print X[i].rjust(int(e)),Y[i].rjust(int(e)),Z[i].rjust(int(e)),m[i].rjust(int(e))


