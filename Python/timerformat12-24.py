import string
a=raw_input()
a=a.split(":")
b=string.find(a[2],"AM")
print b
if b>=0:
    if a[0]=='12':
        a[0]='00'
        a=":".join(a)
    else:
        a=":".join(a)
else:
    if a[0]=='12':
        a[0]='12'
        a[0]=str(a[0])
        a=":".join(a)
    else:
        a[0]=int(a[0])+12
        a[0]=str(a[0])
        a=":".join(a)
    


print a[:-2]
