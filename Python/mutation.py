s = raw_input()
i,k = raw_input().split()
print s[:int(i)]+k+s[int(i)+1:]
