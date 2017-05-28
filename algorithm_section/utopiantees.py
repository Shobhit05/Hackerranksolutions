import math
T=int(input())
d=[0]*T
for i in range(0,T):
    d[i]=int(input())

x=[]
e=0
for c in d:
    n=c//2
    a=int(math.pow(2,n+1)-1)
    if c%2!=0:
        a=a*2
    x.append(a)
    
    
            
            
        
        
print x
    
    
    
