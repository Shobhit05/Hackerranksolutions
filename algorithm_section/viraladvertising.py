T=int(input())
x=[]
c=5
for i in range(0,T):
    c=c//2
    x.append(c)
    c=c*3
print sum(x)
    
