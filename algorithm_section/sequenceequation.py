n=int(input())
f=map(int,raw_input().split())
c=[0]*1
for i in f:
    c.append(i)

x=[]
for i in range(1,n+1):
    d=c.index(c.index(i))
    x.append(d)


for i in x:
    print i
