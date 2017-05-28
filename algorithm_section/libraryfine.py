A,B,C=map(int,raw_input().split())
D,E,F=map(int,raw_input().split())
if C>F:
    f=10000
elif C==F:
    if B>E:
        f=500*(B-E)
    elif B==E:
        if A>D:
            f=15*(A-D)
        else:
            f=0
    else:
        f=0
else:
    f=0
        
print f    
