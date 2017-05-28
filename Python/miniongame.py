from itertools import combinations
S=raw_input()

d=[]
for i in S:
    d.append(i)

e=[]

f=0
while f<len(d):
    c=len(d)
    while c>0:
        S=""
        for i in range(f,c):
            S=S+str(d[i])
        
        if len(S)>0:
            e.append([S])
        c=c-1
    f=f+1


c=0
for i in e:
    for k in i :
        if k[0]=='A':
            c=c+1
        if k[0]=='E':
            c=c+1
        if k[0]=='I':
            c=c+1
        if k[0]=='O':
            c=c+1
        if k[0]=='U':
            c=c+1


d=len(e)-c


if c>d:
    print "Kevin"+" "+str(c)
elif d>c:
    print "Stuart"+" "+str(d)

else:
    print "Draw"

