print("Read File !!")
# Open File
f=open("hello.txt","w")

data="hardik Vala"
f.write(data)
print(type(data))
print(data)

f.close()

f2=open("hello.txt","r")
data2=f2.read()
for i in data2:
    print(i)


        
# Close file
f2.close()