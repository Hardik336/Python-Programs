# 11.Write a program to create function which shall accept any number of arguments and display total of all the numbers given as argument.

def display(*args):
    total=0
    for i in args:
        total=total+i
    print("Total of all numbers:",total)

display(12,2,3,4,5,6,7)
    