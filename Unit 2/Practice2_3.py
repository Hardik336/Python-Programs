# 3) Write a program to generate arithmetic exception and log the exception in system.

import logging

logging.basicConfig(
    filename="error_info.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class InvalidAgeError(Exception):
    pass

try:
    age=int(input("Enter your age:"))
    
    if age<18:
        raise InvalidAgeError("You must be 18 yers old !!")
    
    print("Access Granted !!")
    
except InvalidAgeError as e:
    print("Custom exceptin occured:",e)
    logging.error("Custom Exception",exc_info=True)

except ValueError as e:
    print("Enter valid value:",e)
    logging.error("ValueError occured",exc_info=True)
    
finally:
    print("Program finished !")
    