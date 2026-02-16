# 7. Write a program to create a list and perform various operations on list
# using menu.

lst =[]
while True:
    print("LIST OPERATIONS MENU")
    print("1. Create List")
    print("2. Display List")
    print("3. Insert Element")
    print("4. Delete Element")
    print("5. Search Element")
    print("6. Sort List")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice==1:
        n = int(input("How many elements? "))
        lst.clear()
        for i in range(n):
            ele = int(input(f"Enter element {i+1}: "))
            lst.append(ele)
        print("List created successfully.")

    elif choice==2:
        print("List elements:", lst)

    elif choice==3:
        ele = int(input("Enter element to insert: "))
        lst.append(ele)
        print("Element inserted.")

    elif choice==4:
        ele = int(input("Enter element to delete: "))
        if ele in lst:
            lst.remove(ele)
            print("Element deleted.")
        else:
            print("Element not found.")

    elif choice==5:
        ele = int(input("Enter element to search: "))
        if ele in lst:
            print("Element found at index:", lst.index(ele))
        else:
            print("Element not found.")

    elif choice==6:
        lst.sort()
        print("List sorted.")

    elif choice==7:
        print("Program exited.")
        break

    else:
        print("Invalid choice! Try again.")

    