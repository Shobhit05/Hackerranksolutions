n=int(input())
a=map(int,raw_input().split())
f=0
while len(a)>=0 and a.count(1)>0:
    f=f+(a.index(1))/2
    f=f+1
    a=a[a.index(1)+1:]

if len(a)>1:
    f=f+len(a)/2

print f    
    
    
