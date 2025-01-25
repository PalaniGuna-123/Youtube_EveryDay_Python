# Problem 1)   Write a Python function to calculate the sum Array
def findSum(arr):
    sum=0
    for i in arr:
        sum+=i
    print(sum)

findSum([1,2,3,45,6])



#Question  2 Calculate the Average of an Array
def findAvg(arr):
    sum=0
    for num in arr:
        sum+=num
    avg=sum/len(arr)
    print(avg)

findAvg([12,12,12,12])



        

#  Question 3    Find the Maximum Value in an Array
def findMax(arr):
    maximum=arr[0]
    for num in arr:
        if num>maximum:
            maximum=num
    print(maximum)

findMax([1,2,3,4,1,1])


# Question 4 Find the Minimum Value in an Array
def findMin(arr):
    minimum=arr[0]
    for num in arr:
        if num<minimum:
            minimum=num
    print(minimum)

findMin([43,87,9,1,24])

