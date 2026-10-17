
from student import (
    Student,
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    show_statistics
)


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Statistics")
    print("7. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        try:
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ").strip()
            marks = int(input("Enter Marks (0-100): "))

            if student_id <= 0:
                print("Student ID must be positive.")
            elif not name:
                print("Student name cannot be empty.")
            elif not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
            else:
                student = Student(student_id, name, marks)
                add_student(student)

        except ValueError:
            print("Please enter valid numeric values.")

    elif choice == "2":
        view_students()

    elif choice == "3":
        try:
            student_id = int(input("Enter Student ID to search: "))
            search_student(student_id)
        except ValueError:
            print("Please enter a valid Student ID.")

    elif choice == "4":
        try:
            student_id = int(input("Enter Student ID to update: "))
            name = input("Enter new name: ").strip()
            marks = int(input("Enter new marks (0-100): "))

            if student_id <= 0:
                print("Student ID must be positive.")
            elif not name:
                print("Student name cannot be empty.")
            elif not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
            else:
                update_student(student_id, name, marks)

        except ValueError:
            print("Please enter valid numeric values.")

    elif choice == "5":
        try:
            student_id = int(input("Enter Student ID to delete: "))

            confirm = input(
                "Are you sure you want to delete this student? (yes/no): "
            ).strip().lower()

            if confirm == "yes":
                delete_student(student_id)
            else:
                print("Delete cancelled.")

        except ValueError:
            print("Please enter a valid Student ID.")

    elif choice == "6":
        show_statistics()

    elif choice == "7":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Select a number from 1 to 7.")
