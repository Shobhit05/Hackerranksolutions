s=raw_input()
s=list(s)
d=0
a=['S','O','S']
for i in range(0,len(s),3):
    c=s[i:i+3]
    for i in range(0,3):
        if c[i]!=a[i]:
            d=d+1
        
    

print d
