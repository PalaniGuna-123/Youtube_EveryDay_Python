n=5 
for i in range (1,n+1):
    for j in range (i):
        print("* ",end="")
    print()


#Right Angle Triangle RIght Aligned

n=5
for i in range (1,n+1):
    for j in range(n-i): #Print spaces before star
        print(" ",end="")
    for k in range(i):
        print("*", end ="")
    print()

    ## Right ANgel numbers triangle

rows=5
count=1
for i in range (1,rows+1):
    for j in range(1,i+1):
        print(count,end=" ")
        count+=1
    print()

#5 Right Angle triangle in  numbers
rows=5
for i in range (1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#6 Right Angle triangle in alphabets

rows=7
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()