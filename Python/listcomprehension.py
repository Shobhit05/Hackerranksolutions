##from itertools import product
##X=int(input())
##Y=int(input())
##Z=int(input())
##N=int(input())
##
##list1=[0,X,Y,Z]
##list2=[]
##for i in (0,X):
##    print i
##    for j in (0,Y):
##        print j
##        for k in (0,Z):
##            print k
##            if i+j+k!=N:
##                if list2.count([i,j,k])==0:
##                    list2.append([i,j,k])
##
##print list2
X=int(input())
Y=int(input())
Z=int(input())
N=int(input())
list2=[]
for i in range(0,X+1):
    print i
    for j in range(0,Y+1):
        print j
        for k in range(0,Z+1):
            print k
            if i+j+k!=N and list2.count([i,j,k])==0:
                list2.append([i,j,k])
        
print list2        

