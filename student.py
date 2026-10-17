
import sqlite3


DATABASE_NAME = "student.db"


class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        return "D"


def connect_db():
    connection = sqlite3.connect(DATABASE_NAME)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            marks INTEGER NOT NULL
                CHECK (marks BETWEEN 0 AND 100)
        )
    """)

    connection.commit()
    return connection


def add_student(student):
    connection = connect_db()

    try:
        connection.execute(
            "INSERT INTO students (student_id, name, marks) "
            "VALUES (?, ?, ?)",
            (student.student_id, student.name, student.marks)
        )
        connection.commit()
        print("Student added successfully!")

    except sqlite3.IntegrityError:
        print("Student ID already exists or marks are invalid.")

    finally:
        connection.close()


def view_students():
    connection = connect_db()

    records = connection.execute(
        "SELECT * FROM students ORDER BY student_id"
    ).fetchall()

    connection.close()

    if not records:
        print("No student records found.")
        return

    print("\n" + "-" * 55)
    print(f"{'ID':<10}{'Name':<22}{'Marks':<10}{'Grade'}")
    print("-" * 55)

    for record in records:
        student = Student(*record)
        print(
            f"{student.student_id:<10}"
            f"{student.name:<22}"
            f"{student.marks:<10}"
            f"{student.calculate_grade()}"
        )

    print("-" * 55)


def search_student(student_id):
    connection = connect_db()

    record = connection.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,)
    ).fetchone()

    connection.close()

    if record:
        student = Student(*record)
        print("\n--- Student Found ---")
        print("ID:", student.student_id)
        print("Name:", student.name)
        print("Marks:", student.marks)
        print("Grade:", student.calculate_grade())
    else:
        print("Student not found.")


def update_student(student_id, name, marks):
    connection = connect_db()

    cursor = connection.execute(
        "UPDATE students SET name = ?, marks = ? "
        "WHERE student_id = ?",
        (name, marks, student_id)
    )

    connection.commit()
    updated = cursor.rowcount
    connection.close()

    if updated:
        print("Student details updated successfully!")
    else:
        print("Student not found.")


def delete_student(student_id):
    connection = connect_db()

    cursor = connection.execute(
        "DELETE FROM students WHERE student_id = ?",
        (student_id,)
    )

    connection.commit()
    deleted = cursor.rowcount
    connection.close()

    if deleted:
        print("Student deleted successfully!")
    else:
        print("Student not found.")


def show_statistics():
    connection = connect_db()

    result = connection.execute("""
        SELECT
            COUNT(*),
            AVG(marks),
            MAX(marks),
            MIN(marks)
        FROM students
    """).fetchone()

    connection.close()

    total, average, highest, lowest = result

    print("\n--- Student Statistics ---")
    print("Total Students:", total)

    if total == 0:
        print("No records available for statistics.")
        return

    print(f"Average Marks: {average:.2f}")
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)
