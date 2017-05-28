n=int(input())
c=map(int,raw_input().split())
b=set(c)
f=n+1
if len(b)<len(c):
    for i in b:
        if c.count(i)>1:
            x=c.index(i)
            y=c.index(i,x+1)
            z=abs(x-y)
            if z<f:
                f=z
else:
    f=-1
        
print f

