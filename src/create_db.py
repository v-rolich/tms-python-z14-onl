import data_db as db
import sqlite3

con = sqlite3.connect('MyDB.db')

cur = con.cursor()

cur.execute('''CREATE TABLE Department
               (id int PRIMARY KEY, name text)''')

cur.execute('CREATE TABLE Teacher\n'
            '               (id int PRIMARY KEY, first_name text, last_name text, \n'
            '               phone_number int, department int,\n'
            '               FOREIGN KEY (department) REFERENCES Department (id))')

cur.execute('''CREATE TABLE Course
               (id int PRIMARY KEY, title text, department int, other_details text,
               FOREIGN KEY (department) REFERENCES Department (id))''')

cur.execute('''CREATE TABLE Section
               (id int PRIMARY KEY, course int, teacher int, capacity text,
               FOREIGN KEY (course) REFERENCES Course (id),
               FOREIGN KEY (teacher) REFERENCES Teacher (id))''')

cur.execute('''CREATE TABLE Student
               (id int PRIMARY KEY, first_name int, last_name int, date_of_birth date,
               phone_number int)''')

cur.execute('''CREATE TABLE Student_section
               (id int PRIMARY KEY, student_id, section_id int,
               FOREIGN KEY (section_id) REFERENCES Section (id),
               FOREIGN KEY (student_id) REFERENCES Student (id))''')

cur.executemany("INSERT INTO Department VALUES (?, ?)", db.Dep_lst)
cur.executemany("INSERT INTO Course VALUES (?, ?, ?, ?)", db.Course_lst)
cur.executemany("INSERT INTO Teacher VALUES (?, ?, ?, ?, ?)", db.Teacher_lst)
cur.executemany("INSERT INTO Section VALUES (?, ?, ?, ?)", db.Section_lst)
cur.executemany("INSERT INTO Student VALUES (?, ?, ?, ?, ?)", db.Student_lst)
cur.executemany("INSERT INTO Student_section VALUES (?, ?, ?)", db.Student_section_lst)

con.commit()
con.close()
