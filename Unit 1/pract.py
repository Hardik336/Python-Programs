
class Hello():
    
    # def __init__(self):
    #     print("Constructor !!")
    
    # def fun1(self):
    #     var=10
    #     print(type(var))
        
    def readFile(self):
        print("Read File !!")
        # Open File
        f=open("hello.txt","r")
        data=f.read()
        print(type(data))
        print(data)
        
        # Close file
        f.close()
        
obj=Hello()
# obj.fun1()
obj.readFile()





              
          




