#1.   Counting spaces in a string
import re
space_count="python is 1"
space_count_full=re.findall("[\ s]",space_count)
print(len(space_count_full))





#2.   Counting Special Cherecters in a string
import re
def count_sp_char(string):
    sp_char="!@#$%^&*()<>??/[]{};:'"
    count=0
    for i in string:
        if i in sp_char:
            count+=1
    print(count)

count_sp_char("HEllo! HOw are you? #special char! 123")









#3. removeing in a white spaces

string="G U N A"
str=string.replace(" ","")
print(str)






# 4.  Adding Two List Elements Togather
list1=[1,2,3]
list2=[4,5,6]
res_1st=[]
for i in range(0,len(list1)):
    res_1st.append(list1[i]+list2[i])

print(res_1st)


