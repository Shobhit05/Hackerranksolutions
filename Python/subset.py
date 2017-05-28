##T=int(input())
##C=[]
##D=[]
##for i in range(0,T):
##    p=int(input())
##    A=map(int,raw_input().split())
##    x=set(A)
##    C.append(x)
##    q=int(input())
##    B=map(int,raw_input().split())
##    y=set(B)
##    D.append(y)
##
##
##for i in range(0,T):
##    print(C[i].issubset(D[i]))
##    



A=set(map(int,raw_input().split()))
N=int(input())
C=[]
for i in range(0,N):
    B=set(map(int,raw_input().split()))
    C.append(B)
q=0
for i in C:
    if i.issubset(A) and len(i)!=len(A):
        q=q+1

if q==len(C):
    print "True"
else:
    print "False"
        
    
    
