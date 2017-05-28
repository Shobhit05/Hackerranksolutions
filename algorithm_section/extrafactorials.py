n=int(input())
def fact(n):
    if n==0:
        return 1
    else:
        n=n*fact(n-1)
        return n

a=fact(n)
print a
