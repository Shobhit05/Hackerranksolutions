from operator import itemgetter
N=int(input())
c=[]
for i in range(0,N):
    fn=map(str,raw_input().split())
    c.append(fn)

D=sorted(c,key=itemgetter(2))




    
for j in D:
    if j[3]=='M':
        print("Mr."+" "+j[0]+" "+j[1])

    else:
        print("Ms."+" "+j[0]+" "+j[1])
        
        
