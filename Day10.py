n=5
#Top part
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()

#bottom part
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range (2*i-1) :
        print("*",end="")
    print()

#Hollow Right Angle Triangle
n=5
for i in range(1,n+1):
    for j in range(i):
        if j==0 or j==i-1 or j==n or j==n-1:  #condition of borders
            print("*", end="")
        else:
            print(" ",end="")
    print()

