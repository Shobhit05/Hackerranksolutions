import numpy
N,M=map(int,raw_input().split())
A=[map(int,raw_input().split()) for i in range(0,N)]
B=[map(int,raw_input().split()) for i in range(0,N)]
a=numpy.array(A)
b=numpy.array(B)
print a+b
print a-b
print a*b
print a/b
print a%b
print a**b
