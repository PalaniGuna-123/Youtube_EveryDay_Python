# 1. Converting an integer into Decimals
import decimal
integer=10
print(decimal.Decimal(integer))
print(type (decimal.Decimal(integer)))



# 2.Converting an string of integers into Decimals
import decimal
string="123"
print(decimal.Decimal(string))
print( type (decimal.Decimal(string)))



# 3. Reverseing a String using an Extended Slicing Technique
string="Guna Vision"
print(string[::-1])


# 4.Counting VOWELS in a Given Word
vowel=['a','e','i','o','u','A','E','I','O','U']
word="Guna VIson"
count=0
for i in word:
    if i in vowel:
        count+=1
print(count)




# 5.Counting Consonants in a Given word
vowel=['a','e','i','o','u','A','E','I','O','U']
word="Guna VIson"
count=0
for i in word:
    if i not in vowel:
        count+=1
print(count)

