##import numpy
##P=map(float,raw_input().split())
##x=int(input())
##
##print numpy.polyval(P,x)

import numpy
A=map(int,raw_input().split())

A.reverse()

arr=numpy.array(A,float)
print arr
