# 8) Write a program to read file which has marks entry of student and display details with total, percentage and grade (Consider a file which has comma separated data with RollNo, Student Name, Mark1, Mark2, Mark3 and Mark4)

# Open file
with open(r"D:\MCA Sem 2 Coding\Python\Syllabus Questions\Unit 2\marks.txt", "r") as f:

    print("RollNo  Name    Total  Percentage  Grade")

    for line in f:
        line = line.strip()

        if not line:
            continue

        data = line.split(",")

        roll = data[0]
        name = data[1]

        m1 = int(data[2])
        m2 = int(data[3])
        m3 = int(data[4])
        m4 = int(data[5])

        total = m1 + m2 + m3 + m4
        percentage = total / 4

        # Grade calculation
        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        else:
            grade = "D"

        # Display result
        print(roll, name, total, percentage, grade)

