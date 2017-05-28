n=int(input())
c=map(int,raw_input().split())
b=set(c)
d=0
for i in b:
    a=c.count(i+1)+c.count(i)
    b=c.count(i)+c.count(i-1)
    if b>a:
        a=b
    if a>d:
        d=a
print d
    
