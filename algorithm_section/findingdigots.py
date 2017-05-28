T=input()
c=[]
d=[]
for i in range(0,T):
    c.append(int(input()))

q=0
f=0
x=[]
for i in c:
    d=list(str(i))
    for k in d:
        if int(k)!=0:
            print f
            if c[f]%int(k)==0:
                q=q+1
    x.append(q)
    f=f+1
    q=0
                
print x    
             
    
