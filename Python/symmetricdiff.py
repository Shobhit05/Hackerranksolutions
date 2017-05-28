M=int(input())
A=map(int,raw_input().split())
N=int(input())
B=map(int,raw_input().split())
a=set(A)
b=set(B)

X=list(a.difference(b))
Y=list(b.difference(a))
for i in Y:
    X.append(i)

X.sort()
for j in X:
    print j
