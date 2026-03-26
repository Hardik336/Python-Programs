# 6) Write a program to read a file which contains only numbers. Display total of all numbers with maximum and minimum number.


file=open("D:/MCA Sem 2 Coding/Python/Syllabus Questions/Unit 2/numbers.txt","r")
data=file.readlines()
print(data)

lst=[]

for i in data:
    num=int(i.strip())
    lst.append(num)

# print(type(lst))
# print(type(lst[0]))

print(lst)

print("Total",sum(lst))
print("Maximum:",max(lst))
print("Minimum:",min(lst))


