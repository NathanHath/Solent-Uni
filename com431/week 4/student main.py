from student import Student
students = []

for i in range (2):
    student_name = input("Enter student name: ")
    student_ID = input("Enter student ID: ")
    student_course = input("Enter student course: ")
    student_mark = int(input("Enter student mark: "))
    students.append(Student(student_name, student_ID, student_course, student_mark))
    print (students)

