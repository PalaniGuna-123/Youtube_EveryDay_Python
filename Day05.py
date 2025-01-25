# 1.  Comparing Two Strings for ANAGRAMS
str1="listen"
str2="silent"
str1=str1.replace(" ","").upper()
str2=str2.replace(" ","").upper()

if sorted(str1)==sorted(str2):
    print("It is a anagrams")
else:
    print("it is a not anagrams")





# 2. Cheack for PALINDROME using 
str1="guna".lower()
if str1==str1[::-1]:
    print("True")
else:
    print("False")






# 3.  Counting the white spaces in a string 

string=" gun a visio n"
print(string.count(" "))




# 4. Counting Digits sum
#importing Reguler Expressions library
import re
name="subscribe our channel 100"
digitCount=re.sub("[^0-9]","",name)
print(len(digitCount))






# 5.  Counting Letters
import re
name="subscribe our channel 100"
letterCount=re.sub("[^a-zA-Z]","",name)
print(len(letterCount))

