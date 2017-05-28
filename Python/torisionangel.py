import math
import numpy as np
A=map(float,raw_input().split())
B=map(float,raw_input().split())
C=map(float,raw_input().split())
D=map(float,raw_input().split())

a=np.array([A])
b=np.array([B])
c=np.array([C])
d=np.array([D])

AB=b-a
BC=c-b
DC=c-d
X=np.cross(AB,BC)
Y=np.cross(BC,DC)

w=np.linalg.norm(X)
y=np.linalg.norm(Y)
q=w*y
for i in X:
    K=i
for j in Y:
    L=j

s=np.dot(K,L)
s=float(abs(s))/float(q)
d=math.acos(s)
d=math.degrees(d)
X=format(d,'.2f')
print X
