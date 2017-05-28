i,j,k=map(int,raw_input().split())
d=0
for i in range(i,j+1):
    c=list(str(i))
    c.reverse()
    c=''.join(c)
    if (int(i)-int(c))%k==0:
        d=d+1

print d
        
