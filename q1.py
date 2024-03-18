#Student Name: Shawnia Noel
#Student Id: 101207361

import psycopg2

#create a connection with the postgresql database server
#the name of the database we want to access is Students
#the postgresql databse server is on our locolhost at port 5432
#the user is postgres, postgres is the default user, if you don't use postgres user then please change it
#the password should be replaced by whatever your password is
connection = psycopg2.connect(dbname= "Students", user="postgres", password = "REPLACE_WITH_YOUR_PASSWORD", host="localhost",port="5432")

#we create a cursor with the connection we established. the cursor is simply a tool that execute sql commands
cur = connection.cursor()


#we call the function execute on the cursor object, this simply executes the sql command passed as argument
cur.execute("CREATE TABLE IF NOT EXISTS students (student_id SERIAL PRIMARY KEY,first_name TEXT NOT NULL,last_name TEXT NOT NULL,email TEXT NOT NULL UNIQUE,enrollment_date DATE)")

#calling commit() just makes the changes permanent on the actual database. If we don't call commit then the changes made are not actually reflected in our database on the postgresql server
connection.commit()


#execute insert command to insert new data
cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date)VALUES ('John', 'Doe', 'john.doe@example.com', '2023-09-01'), ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'), ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')")

#make the changes permanent
connection.commit()


#have the cursor run the sql query command to find all the students in the table
def getAllStudents():
    cur.execute("SELECT * FROM students")

    #the function fecthall() just return the all the results of the query as a list of tuple
    #we can then go through that list and print every item of the list
    allRecords = cur.fetchall()
    for a_record in allRecords:
        print(a_record)
    print()


#have the cursor run the sql insert command, the relevant data for the new student are passed to the function, the %s means it is a string variable
#call commit() to make the change permanent
def addStudent(first_name, last_name, email, enrollment_date):
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date)VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    connection.commit()


#have the cursor run the sql update command, the student id and new email are passed to the function
#call commit() to make the change permanent
def updateStudentEmail(student_id, new_email):
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    connection.commit()



#have the curson execute an sql delete command,
#call commit() to make the changes permanent
def deleteStudent(student_id):
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    connection.commit()




#create a simple menu for user interaction
def main():
    while True:
        print()
        print("Menu:")
        print("1. View all students")
        print("2. Add a new student")
        print("3. Update a student's email")
        print("4. Delete a student")
        print("0. Exit")
        print()

        choice = input("Your option choice: ")

        #call each relevant function corresponding to the choice entered
        #no data validation is done, it is assumed that user provide valid/non-erronous data


        if choice == "1":
            print("all students records is as follows:")
            getAllStudents()
            print()

        elif choice == "2":
            first_name = input("Input first name of student: ")
            last_name = input("Input last name of student: ")
            email = input("Input email of student: ")
            enrollment_date = input("Input student's enrollment date in format (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)

        elif choice == "3":
            student_id = input("Input the student ID: ")
            new_email = input("new email of student: ")
            updateStudentEmail(student_id, new_email)

        elif choice == "4":
            student_id = input("Enter student ID of student to be deleted: ")
            deleteStudent(student_id)

        elif choice == "0":
            break

        else:
            print("Invalid choice\n")

main()


#when we are done we close the cursor and the connection in that order
cur.close()
connection.close()