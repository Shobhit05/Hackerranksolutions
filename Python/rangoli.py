from __future__ import print_function
N=input()
if 0<N<27:
    for i in range(0,N):
        for j in range(0,N*2-2*(i+1)):
            print ("-",end='')
            
    

        for k in range(0,i+1):
            print(chr(96+N-k),end='')
            if k!=i:
                print ("-",end='')

    

        for l in range(i,0,-1):
            print("-",end='')
            print(chr(96+N-(l-1)),end='')

        for m in range(0,N*2-2*(i+1)):
            print("-",end='')
                

        print("")


    for a in range(1,N):
        for b in range(0,2*a):
            print ("-",end='')

        for c in range(0,N-a):
            print(chr(96+N-c),end='')
            if c!=N-a-1:
                print("-",end='')

        for d in range(N-1-a,0,-1):
            print("-",end='')
            print(chr(96+N-(d-1)),end='')
        
        for e in range(0,2*a):
            print("-",end='')

        print(" ")


else:
    exit
        
     
    
    

    



