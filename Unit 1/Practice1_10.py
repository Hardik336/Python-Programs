# 10.Write a program to create 4 lambda functions which shall accept 2 numbers and one arithmetic operator. As per arithmetic operator related lambda functions shall be invoked.

# Lambda functions
add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b if b != 0 else "Division by zero not allowed"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter arithmetic operator (+, -, *, /): ")

if op == '+':
    print("Result:", add(num1, num2))
elif op == '-':
    print("Result:", sub(num1, num2))
elif op == '*':
    print("Result:", mul(num1, num2))
elif op == '/':
    print("Result:", div(num1, num2))
else:
    print("Invalid operator")
