#1)  Write function named "fizzBuzz(num)" which prints Fizz if the number is a multiple of 3, Buzz if its a multiple of 5, FizzBuzz
#  it is a multiple of both 3 and 5 else print the number
def fizzBUzz(num):
    if num % 3 ==0 and num %5 ==0:
        print("fizzBUzz")
    elif num % 3==0:
        print ("Fizz")
    elif num % 5==0:
        print("Buzz")
    else:
        print(num)
    
fizzBUzz(20)
fizzBUzz(15)
fizzBUzz(3)


#2)  Find the maximum between 3 numbers a, b, c

# Complete the function to print the maximum between the arguments passed

# maxInThree(3,5,7) and output should be 7
def maximum(a,b,c):
    if(a>b and a>c):
        print(a)
    elif(b>a and b>c):
        print(b)
    else:
        print(c)
maximum(1,2,3)

# Write a Python program to convert a temperature from Celsius to Fahrenheit.
# Fahrenheit = (9/5) x Celsius + 32
celsius=6
Fahrenheit=9/5 * celsius +32
print(Fahrenheit)

#4) Given a year. Check if its a leap year or not

# Example

# 1900: Not a Leap Year

# 1604: Leap Year

def check(year):
    if(year % 4==0 and  not year %100==0 or year % 400 ==0):
        print("It is a leap year")
    else:
        print("NOt a leap Year")

check(1900)
check(1604)

#5)Given a value N find the factorial N! = 1 x 2 x 3 x .... x N - 1 x N
 
# Eg 5! = 1 x 2 x 3 x 4 x 5 and the answer = 120

def factorial(N):
    fact=1
    for i in range (1,N+1):
        fact*=i
    print(fact)
factorial(3)
factorial(5)

def facto(N):
    fact=1
    for i in range(1,N+1):
        fact*=i
    print(fact)
 



 

