a=raw_input()
b=raw_input()
k=int(input())
d=-2
if set(a)!=set(b):
    for i in range(0,len(a)):
        if a[i]!=b[i]:
            d=i
            e=i
            break
    if d==-2:
        if abs(len(b)-len(a)-k)%2==0:
            print "Yes"
        else:
            print "No"
    elif d==0:
        if len(a)%k==0:
            print "No"
        else:
            print "Yes"
    else:
        if k==len(a)-d+len(b)-e:
            print "Yes"
        else:
            print "No"
elif set(a)==set(b):
    print "Yes"

print len(a)

