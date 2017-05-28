from __future__ import print_function
s=raw_input()
k=int(input())
n=len(s)
d=n/k
e=[]
for i in s:
    e.append(i)

f=[]
m=0
for i in range(0,d):
    f.append(e[m:m+k])
    m=m+k
    
    
for p  in f:
    for k in p:
        c=p.count(k)
        for l in range(0,c):
        
            p.remove(k)
        p.insert(0,k)
    p.reverse()

for q in f:
    for s in q:
        print(s,end='')
    print("")
            
            


