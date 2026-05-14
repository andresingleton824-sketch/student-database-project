# Author: Andre Singleton & Makenzie Totushek
# Date: 5/5/26
# Name: Create Student Database

import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('student.db')

    # Get a database cursor.
    cur = conn.cursor()

    # Add the sample students table.
    sample_students_table(cur)

    # Add rows to the students table.
    add_students(cur)

    # Commit the changes.
    conn.commit()

    # Display the students.
    display_sample_students(cur)

    # Close the connection.
    conn.close()

def sample_students_table(cur):
    # If the table already exists, drop it.
    cur.execute('DROP TABLE IF EXISTS sample_students')

    # Create the table.
    cur.execute('''CREATE TABLE sample_students (student_id int PRIMARY KEY NOT NULL,
                                        first_name TEXT,
                                        last_name TEXT,
                                        grade TEXT,
                                        major TEXT,
                                        email TEXT,
                                        phone_number TEXT)''')

def add_students(cur):
    # student info
    sample_students_pop = [
        (
            # student id
            1001,
            # first name
            "Emma",
            # last name
            "Johnson",
            # grade
            "A",
            # major
            "Computer Science",
            # email
            "emma.j@school.edu",
            # phone number
            "612-555-0101"),
        (
            # student id
            1002,
            # first name
            "Liam",
            # last name
            "Martinez",
            # grade
            "B+",
            # major
            "Business",
            # email
            "liam.m@school.edu",
            # phone number
            "651-555-0188"
        ),
        (
            # student id
            1003,
            # first name
            "Sophia",
            # last name
            "Nguyen",
            # grade
            "A-",
            # major
            "Biology",
            # email
            "sophia.n@school.edu",
            # phone number
            "763-555-0234"
    )
    ]
    for row in sample_students_pop:
        cur.execute('''INSERT INTO sample_students (student_id, first_name, last_name, grade, major, email, phone_number)
                       VALUES (?, ?, ?, ?, ?, ?, ?)''', (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
 

def display_sample_students(cur):
    print('Contents of student.db/sample_students table:')
    cur.execute('''SELECT * FROM sample_students''')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]}')


if __name__ == "__main__":
    main()
