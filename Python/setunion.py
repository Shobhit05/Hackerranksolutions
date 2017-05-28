##n=int(input())
##A=map(int,raw_input().split())
##b=int(input())
##B=map(int,raw_input().split())
##X=set(A)
##Y=set(B)
##
##Z=X.union(Y)
##print len(Z)
##
##
##n=int(input())
##A=map(int,raw_input().split())
##b=int(input())
##B=map(int,raw_input().split())
##X=set(A)
##Y=set(B)
##
##Z=X.intersection(Y)
##print len(Z)


##
##n=int(input())
##A=map(int,raw_input().split())
##b=int(input())
##B=map(int,raw_input().split())
##X=set(A)
##Y=set(B)
##
##Z=X.difference(Y)
##print len(Z)


n=int(input())
A=map(int,raw_input().split())
b=int(input())
B=map(int,raw_input().split())
X=set(A)
Y=set(B)

Z=X.symmetric_difference(Y)
print len(Z)
