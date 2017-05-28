# Enter your code here. Read input from STDIN. Print output to STDOUT
import string
S=raw_input()
a=S.split(" ")
c=[]
for i in a:
    c.append(string.capitalize(i))

c=" ".join(c)
print c
