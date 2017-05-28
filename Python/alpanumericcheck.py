s=raw_input()
v=len(s)
for a in s:
    z=0
    z=z+1
    if a.isalnum():
        
        print(a.isalnum())
        break
    if z==v:
        if a.isalnum():
            print(a.isalnum())
            break
        else:
            print False
            break


for a in s:
    c=0
    c=c+1
    if a.isalpha():
        print(a.isalpha())
        break
    if c==v:
        if a.isalpha():
            print(a.isalpha())
            break
        else:
            print False
            break
for a in s:
    e=0
    e=e+1
    if a.isdigit():
        print(a.isdigit())
        break
    if e==v:
        if a.isdigit():
            print(a.isdigit())
        else:
            print False
            break
for a in s:
    f=0
    f=f+1
    if a.islower():
        print(a.islower())
        break
    if f==v:
        if a.islower():
            print(a.islower())
            break
        else:
            print False
            break
for a in s:
    g=0
    g=g+1
    if a.isupper():
        print(a.isupper())
        break
    if g==v:
        if a.isupper():
            print(a.isupper())
            break
        else:
            print False
            break

