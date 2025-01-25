#pyramid of NUmbers

n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end=" ")
    print()

#pascal's Triangle
n=7
for i in range(n):
    num=1
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
       print(num,end=" ")
       num=num*(i-j)//(j+1)
    print()
