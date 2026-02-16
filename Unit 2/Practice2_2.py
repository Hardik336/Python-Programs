# 2) Write a program to execute user defined exception in python.

# Custom exceptin class
class InvalidAgeError(Exception):
    pass 

try:
    age=int(input("Enter your age:"))
    
    if age<18:
        raise InvalidAgeError("You must be 18 yers old !!")
    
    print("Access Granted !!")
    
except InvalidAgeError as e:
    print("Custom exceptin occured:",e)

except ValueError as e:
    print("Enter valid value:",e)
    
finally:
    print("Program finished !")
    