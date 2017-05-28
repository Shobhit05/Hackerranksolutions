##import numpy
##N,M=map(int,raw_input().split())
##A=[map(int,raw_input().split()) for i in range(0,N)]
##arr=numpy.array(A)
##X=numpy.sum(arr,axis=0)
##
##
##print numpy.product(X)

##
##import numpy
##N,M=map(int,raw_input().split())
##A=[map(int,raw_input().split()) for i in range(0,N)]
##arr=numpy.array(A)
##X=numpy.min(arr,axis=1)
##
##
##print numpy.max(X)


##import numpy
##N,M=map(int,raw_input().split())
##A=[map(int,raw_input().split()) for i in range(0,N)]
##arr=numpy.array(A)
##print numpy.mean(arr,axis=1)
##print numpy.var(arr,axis=0)
##print numpy.std(arr,axis=None)

import numpy

N=int(input())
A=[map(int,raw_input().split()) for i in range(0,N)]
B=[map(int,raw_input().split()) for i in range(0,N)]

a=numpy.array(A)
b=numpy.array(B)
print numpy.dot(a,b)


