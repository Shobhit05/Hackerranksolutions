T=int(input())
c=[]
d=[]
x=[]
e=0
for i in range(0,T):
    N,K=map(int,raw_input().split())
    c.append([N,K])
    d.append(map(int,raw_input().split()))
f=0  
for i in d:
    for j in i:
        if j<=0:
            e=e+1
    if e>=c[f][1]:
        x.append("NO")
    else:
        x.append("YES")
    f=f+1
    e=0
   
for i in x:
    print i
