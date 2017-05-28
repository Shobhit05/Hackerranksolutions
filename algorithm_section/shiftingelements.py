n,k,q=map(int,raw_input().split())
a=map(int,raw_input().split())
c=[]
for i in range(0,q):
    c.append(int(input()))
    
d=[0]*len(a)
for i in range(0,len(a)):
    d[(i+k)%len(a)]=a[i]

for i in c:
    print d[i] 
