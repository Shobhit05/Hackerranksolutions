n,p=map(int,raw_input().split())

a=map(int,raw_input().split())
e=[]
for j in a:
    d=j/p
    if j%p==0:
        for k in e:
            if k!=d:
                e.append(d)
            else:
                e.append(d+1)
    else:
        e.append(d+1)
        


print e
