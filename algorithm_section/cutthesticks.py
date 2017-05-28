N=int(input())
c=map(int,raw_input().split())
while(len(c)>0):
    d=min(c)
    c=[k-d for k in c]
    print len(c)
    for i in range(0,c.count(0)):
        c.remove(0)
    
