# 1) Write a program to display basic exception handling in python.1) Write a program to display basic exception handling in python.

# # Syntax
# try:
#     # 
# except:
#     # 
# except:
#     # 
# else:
#     # 
# finally:
#     # 
    
try:
    
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result is:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid integer values.")

except Exception as e:
    print("Unexpected Error:", e)

else:
    print("Division successful.")

finally:
    print("Program finished.")
    
    
    
    
    


