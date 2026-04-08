# 9) Write a program to do student operations using menu as follows
# a) Add Student
# b) Search Student
# c) List All Students
# d) Update Student
# e) Delete Student
# f) Exit


students={}


while True:
    
    print("----STUDENT MENU----")
    print("1. Add Student")
    print("2. Search Student")
    print("3. List All Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    
    choice=int(input("Enter your choice:"))
    
    # Add Student
    if choice == 1:
        roll=input("Enter Roll No: ")
        name=input("Enter Name: ")
        students[roll]=name
        print("Student added successfully")
        print(students.items())

    # Search Student
    elif choice == 2:
        roll=input("Enter Roll No: ")
        if roll in students:
            print("Student found:",students[roll])
        else:
            print("Student not found !")
    
    # List All Student
    elif choice == 3:
        print("All Students")
        for roll,name in students.items():
            print(roll,":",name)

    # Update Student
    elif choice == 4:
        roll=input("Enter Roll no to update:")
        if roll in students:
            name=input("Enter new name:")
            students[roll]=name
            print("Student updated.")
        else:
            print("Student not found !!")
            
    # Delete Student 
    elif choice == 5:
        roll=input("Enter Roll No to Delete")
        if roll in students:
            del students[roll]
            print("Student deleted ")
        else:
            print("Student not found")
            
    # Exit
    elif choice == 6:
        print("Exit from Program")
        break
    
    else:
        print("Invalid Choice!")