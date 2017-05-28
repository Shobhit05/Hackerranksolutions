N=int(input())
a=[]
for i in range(0,N):
    c=raw_input()
    c=c[-10:]
    
    a.append(c)

a.sort()

for j in a:
    print("+91"+" "+j[:5]+" " +j[-5:])
    
