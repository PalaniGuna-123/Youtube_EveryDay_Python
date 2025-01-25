#Hollow Diamond

n=5
#top part
for i in range (1,n+1):
    for j in range (n-i):
        print(" ",end="")
    for k in range (2*i-1):
        if k==0 or k==2*i-2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
#bottom part
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        if k==0 or k==2*i-2:
            print("*",end="")
        else:
            print(" ",end="")
    print()

#Right Arrow
n=5
#Upper Part
for i in range(1,n+1):
    for j in range(i): #print increasing stars
        print("* ",end="")
    print()

#Lower part
for i in range(n-1,0,-1):
    for j in range(i):  # Print decreasing order start
        print("* ",end="")
    print()

