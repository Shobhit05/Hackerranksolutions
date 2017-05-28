n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))
E=100
f=0

if c[k%n]==0:
    E=E-1
elif c[k%n]==1:
    E=E-3
i=(2*k)%n
while(i!=0):
    if c[i]==0:
        E=E-1
    elif c[i]==1:
        E=E-3
    i=(i+k)%n
if k!=n:
    if c[0]==0:
        E=E-1
    else:
        E=E-3

print E
