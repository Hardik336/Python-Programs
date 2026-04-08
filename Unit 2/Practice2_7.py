# 7) Write a program to copy a text file using file handling mechanism.

readfile=open("D:/MCA Sem 2 Coding/Python/Syllabus Questions/Unit 2/numbers.txt","r")
writefile=open("copy.txt","w")

data=readfile.read()
writefile.write(data)

print("File copied !!")

readfile.close()
writefile.close()