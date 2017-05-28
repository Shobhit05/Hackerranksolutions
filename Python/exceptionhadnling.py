T=int(input())
d=[]
for i in range(0,T):
    a,b=map(str,raw_input().split())
    d.append([a,b])

for j in d:
    try:
        print(int(j[0])/int(j[1]))
    except ZeroDivisionError as e:
        print "Error Code:",e
    except ValueError as f:
        print "Error Code:",f
        
