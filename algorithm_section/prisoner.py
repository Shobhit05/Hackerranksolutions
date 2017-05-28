T=int(input())
c=[]
for i in range(0,T):
    N,M,S=map(int,raw_input().split())
    c.append([N,M,S])
e=[]

for i in c:
    f=(i[1]+i[2]-1)%(i[0])
    if f==0:
        e.append(i[0])
    else:
        e.append(f)
    
for i in e:
    print i
   




    
