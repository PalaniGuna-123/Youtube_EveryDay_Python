# 1. Counting the umber of occurances of a charecter in a string "programming"
word="programming"
char="g"
count=0
for i in word:
    if i==char:
        count+=1
print(count)






# 2. Writing FIBONACCI Series
fib=[0,1]
n=7
for i in range(n):
    fib.append(fib[-1]+fib[-2])
print(", ".join(str(e) for e in fib))





# 3. Finding the middle Element in an array 
numlist=[12,23,45,67,90]
midElement=int(len(numlist)/2)
print(numlist[midElement])


# 4.  converting a list into a String 
list=['s','u','b','s','c','r','i','b','e']
string="".join(list)
print(string)
print(type(string))



