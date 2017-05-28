from __future__ import division
N=int(input())
D=[i for i in raw_input().split()]
K=int(input())
e=D.count('a')
f=1
d=N-e
for i in range(0,K):
    f=(d/N)*f
    d=d-1
    N=N-1
print(1-f)
    
