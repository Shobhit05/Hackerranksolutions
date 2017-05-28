a=raw_input()
n=int(input())
c=n/len(a)
d=a.count('a')*c
a=a[:n%len(a)]
d=d+a.count('a')
print d
