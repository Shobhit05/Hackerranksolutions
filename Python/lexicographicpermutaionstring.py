from __future__ import print_function
from itertools import combinations_with_replacement
S,k=raw_input().split()
S=sorted(S)
S="".join(S)
list1=list(combinations_with_replacement(S,int(k)))


for i in list1:
    for j in i:
        print(j,end='')
    print("")
