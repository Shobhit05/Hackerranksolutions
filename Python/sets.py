N=int(input())

A=map(int,raw_input().split())

D=set(A)
S=0
for i in D:
    S=S+i
print S
X=float(S)/len(D)
print X
