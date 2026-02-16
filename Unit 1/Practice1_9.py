# 9. Write a program to create a function which accepts 2 numbers and one arithmetic operator. Return the answer accordingly.

def arithOp(val1,val2,optr):
    match optr:
        case "+":
            print(val1+val2)
        case "-":
            print(val1-val2)
        case "*":
            print(val1*val2)
        case "/":
            print(val1/val2)
        case "%":
            print(val1%val2)
            
arithOp(5,10,'%')