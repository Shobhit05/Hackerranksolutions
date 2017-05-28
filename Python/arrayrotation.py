n,d,q=map(int,raw_input().split())
A=map(int,raw_input().split())
C=[]
for i in range(0,d):
    C=[]
    for k in range(0,len(A)):
        C.insert(n-1-k,A[k])
    A=C

B=[]
for i in range(0,q):
    B.append(int(input()))
    
             

for i in B:
    print C[i]

