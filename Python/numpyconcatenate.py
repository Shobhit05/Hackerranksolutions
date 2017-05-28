import numpy

N,M,P=map(int,raw_input().split())

l=[map(int,raw_input().split()) for x in range(0,N)]

m=[map(int,raw_input().split()) for x in range(0,M)]

print numpy.concatenate((l, m), axis = 0)
