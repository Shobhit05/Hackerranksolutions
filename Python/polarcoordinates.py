import cmath
a=raw_input()
d=a.split("+")

D=abs(complex(int(d[0]),int(d[1][:-1])))
E=cmath.phase(complex(int(d[0]),int(d[1][:-1])))

##D=format(D,'.3f')
##E=format(E,'.3f')
print D
print E
