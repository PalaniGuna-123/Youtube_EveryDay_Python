#1.  Remove duplicates from an Array. You are allowed to use libraries. Please handle None and Empty array cases. For such cases please print empty string.



#example  remove_duplicates([1,2,2,3,4])  result 1 2 3 4
def remove_duplicates(arr):
    if not arr:
        print(" ")
        return
    result=[]
    for i in arr:
        if i not in result:
            result.append(i)
    print(" ".join(map(str,result)))
remove_duplicates([1,2,2,3,4]) 


#2.  Given an Array of integers find the maximum in an array 
#you are allowed to use libraries. Please check for 0 length and Null cases.
#maxInArray([6,1,3])   
def maxInArray(arr):
    if arr is None or len(arr)==0:
        print()
        return
    print(max(arr))
maxInArray([6,1,3])   






#3. count_word_occurrences ("the quick brown fox jumps over the lazy dog", "the")
def count_word_occurrences(word,target):
    a=word.split(" ")
    count=0
    for i in range(0,len(a)):
        if a[i]==target:
            count+=1
    print(count)

count_word_occurrences ("the quick brown fox jumps over the lazy dog  the", "the")






