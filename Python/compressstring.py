from itertools import groupby
S=raw_input()
a=[]
##D=[k for k ,g in groupby(S)]
##print D
##for i in range(0,len(D)):
##    c=S.count(D[i])
##    a.append([c,D[i]])
##    
##             
##print a
E=[list(g) for k, g in groupby(S)]
for i in E:
    c=len(i)
    d=i[0]
    a.append((c,int(d)))
print a
for i in a:
    print i,
