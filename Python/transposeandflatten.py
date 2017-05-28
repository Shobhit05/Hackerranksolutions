import numpy
N,M=map(int,raw_input().split())

arr=[map(int,raw_input().split()) for i in range(0,N)]

arr1=numpy.array(arr)
print numpy.transpose(arr1)

print arr1.flatten()
