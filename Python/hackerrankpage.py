n=int(input())
p=int(input())
c=0
d=0
for i in range(1,p+1):
    c=c+1
    if c%2==0:
        d=d+1





e=0
f=0

for j in range(n,p+1,-1):
    e=e+1
    if n%2==0:
        if e%2!=0:
            f=f+1
    else:
        if e%2==0:
            f=f+1


if f>d:
    print d
else:
    print f
