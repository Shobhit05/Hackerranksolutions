s,t=map(int,raw_input().split())
a,b=map(int,raw_input().split())
m,n=map(int,raw_input().split())
orange=map(int,raw_input().split())
apple=map(int,raw_input().split())
d=0
e=0
for i in orange:
    if s<=a+i<=t:
        d=d+1
for i in apple:
    if s<=b+i<=t:
        e=e+1
        
        
print d       
print e    
