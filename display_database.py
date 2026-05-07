# Author: Andre Singleton & Makenzie Totushek
# Date: 5/7/26
# Name: View/Edit Student Database

import sqlite3

def main():
    # connect the student database
    conn = sqlite3.connect('student.db')

    # get a cursor
    cur = conn.cursor()

    # get student id from user
    s_id = int(input('Enter a student ID or enter "1" to see all: '))

    if s_id == 1:
        # display all students
        cur.execute("SELECT student_id, first_name, last_name, grade, major, email, phone_number from sample_students")
        results = cur.fetchall()
        print(f'The current information is {results}')

    else:
        # find that specific student
        cur.execute("SELECT student_id, first_name, last_name, grade, major, email, phone_number from sample_students WHERE student_id == ?", (s_id,))
        results = cur.fetchone()
        if results == None:
            # Error message if there isn't a student with that number
            print(f"No one with the student ID {s_id} was found")
            return
        else:
            # display specific student
            print(results)

            # ask if they want to update student information
            update = input("Would you like to update the student's information? (y/n) ")
            if update.lower() == 'y':
                # simplify field names
                field_map = {
                    'id': 'student_id',
                    'first name': 'first_name',
                    'last name': 'last_name',
                    'grade': 'grade',
                    'major': 'major',
                    'email': 'email',
                    'phone number': 'phone_number'}

                while update == 'y':
                    # ask which field to update
                    field = input('Which field would you like to update? (id, first name, last name, grade, major, email, or phone number): ').lower()
                    # Error message if not a valid field
                    if field not in field_map:
                        retry = input('That is an invalid field name, would you like to try again? (y/n) ')
                        if retry.lower() == 'y':
                            continue
                        else:
                            return

                    column = field_map[field]
                    # get the new information
                    new_info = input(f'Please enter the new information for {field}: ')
                    # update the information
                    query = f'UPDATE sample_students SET {column} = ? WHERE student_id = ? '
                    cur.execute(query, (new_info, s_id))
                    conn.commit()
                    print(f'The student was updated successfully')
                    again = input('Would you like to update another field? (y/n) ')
                    if again.lower() == 'y':
                        continue
                    else:
                        return

            # ask if they want to delete student
            delete = input('Would you like to delete the student from the database? (y/n) ')
            if delete.lower() == 'y':
                cur.execute("DELETE FROM sample_students WHERE student_id == ?", (s_id,))
                conn.commit()
                print(f'The student was deleted')
                return


    # close the connection
    conn.close()
if __name__ == '__main__':
    main()