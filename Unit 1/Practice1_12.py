# 12.Write a program to display the use of local, global and nonlocal variables

x = 10          # Global variable

def outer():
    y = 20      # Nonlocal variable

    def inner():
        z = 30  # Local variable
        nonlocal y
        global x

        x = x + 5
        y = y + 5
        z = z + 5

        print("Inside inner()")
        print("Global x:", x)
        print("Nonlocal y:", y)
        print("Local z:", z)

    inner()
    print("Inside outer() after inner()")
    print("Nonlocal y:", y)

outer()
print("Outside all functions")
print("Global x:", x)
