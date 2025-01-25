#Equilateral triangle
n=5
for i in range(1,n+1):
    for j in range(n-i):  
        print(" ", end="")
    for k in range(2 *i-1):
        print("*",end="")

    print()


# square
n=7
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()

#Hollow square

n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("* ",end="") #print stars for border
        else:
            print("  ",end="")

    print()
