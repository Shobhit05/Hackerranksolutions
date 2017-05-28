
##for i in range(0,K):
##    ai=list([x for x in map(int,raw_input().split())])
##    ai.sort()
##    c.append(ai.pop(-1))
##
##d=0
##for j in c:
##    d=(j*j)+d
##
##print(d%M)
##    
##print ai



from itertools import product
K,M=map(int,raw_input().split())
a=[map(int,raw_input().split())for x in range(0,K)]
S=0
list1=[]
for m in a:
    m.pop(0)
for k in a:
    list1.append(list(m*m for m in k))




list2=list(product(*list1))


list3=[]
for i in list2:
    i=list(i)
    list3.append(i)

list4=[]
for g in list3:
    Q=0
    for o in g:
        Q=Q+o
    list4.append(Q%M)

list4.sort()
print list4.pop()

















##list2=list(product(*a))
##print list2

##from itertools import product
##list1=[1,4,2]
##list2=[2,3,4]
##list3=[2,43]
##
##B=[list1,list2,list3]
##print list(product(*B))








    

##    c.append(j.pop(-1))
##S=0
##for k in c:
##   S=(k*k)+S
##
##print(S%M)

