from collections import Counter
X=int(input())
b=[x for x in map(int,raw_input().split())]
N=int(input())
a=[map(int,raw_input().split())for x in range(0,N)]

print a
print Counter(b)

