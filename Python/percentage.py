import math
N=int(input())
A=[]
for i in range(0,N):
    A.append(map(str,raw_input().split()))




name=raw_input()


for i in A:
    if name==i[0]:
        c=A.index(i)

print c
D= A[c][1:]
print D      
S=0
for j in D:
    S=S+float(j)


X=float(S/len(D))
X=format(X,'.2f')
print X

