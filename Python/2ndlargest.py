N=int(input())
a=map(int ,raw_input().split())
a.sort()
a.reverse()
##for i in range(0,len(a)-1):
##    if a.pop(i)==a.pop(i+1):
##        
##    else:
##        print a.pop()
##    break
c=a.count(a[0])
if c==len(a):
    print(a[0])
else:
    print(a.pop(c))
#s = raw_input("Please enter your numbers: ")
#mynums = [int(i) for i in s.split()]
#print len(s)
#print mynums
##nums=[i for i in map(int,raw_input().split())]
##print nums

# OR
#mynums = map(int, s.split())


##import sys
##
##lis3=[int(x) for x in sys.argv[5:]]
##lis3=[1,2,4,3,2,4,5]
##print lis3
