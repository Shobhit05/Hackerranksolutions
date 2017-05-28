T=int(input())
c=[]
for i in range(0,T):
    c.append(raw_input())
e=list("ackerrank")
x=[]

for j in range(0,T):
    d=c[j].find('h')
    if d>=0:
        x.append(c[j][d])
    for i in e:
        a=c[j].find(i,d+1)
        d=a
        if a>=0:
            x.append(c[j][a])
    x.append("2")

x=''.join(x)
x=x.split("2")
x.pop()
for i in x:
    if i=="hackerrank":
        print "YES"
    else:
        print "NO"
