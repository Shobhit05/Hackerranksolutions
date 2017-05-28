from __future__ import print_function
from itertools import combinations
S,k=raw_input().split()
S=sorted(S)
S="".join(S)


for a in range(1,int(k)+1):
    
    list1=list(combinations(S,a))
    
    for i in list1:
        for j in i:
            print(j,end='')
        print("")

print(list1)
