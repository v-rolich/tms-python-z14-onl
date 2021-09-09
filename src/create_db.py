import sqlite3
from data_db import Dep_lst, Course_lst, Teacher_lst, Section_lst, Student_lst, Student_section_lst

con = sqlite3.connect('MyDB.db')

cur = con.cursor()

cur.execute('''CREATE TABLE Department
               (id int PRIMARY KEY, name text)''')

cur.execute('''CREATE TABLE Teacher
               (id int PRIMARY KEY, first_name text, last_name text, phone_number int, department int,
               FOREIGN KEY (department) REFERENCES Department (id))''')

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

cur.executemany("INSERT INTO Department VALUES (?, ?)", Dep_lst)
cur.executemany("INSERT INTO Course VALUES (?, ?, ?, ?)", Course_lst)
cur.executemany("INSERT INTO Teacher VALUES (?, ?, ?, ?, ?)", Teacher_lst)
cur.executemany("INSERT INTO Section VALUES (?, ?, ?, ?)", Section_lst)
cur.executemany("INSERT INTO Student VALUES (?, ?, ?, ?, ?)", Student_lst)
cur.executemany("INSERT INTO Student_section VALUES (?, ?, ?)", Student_section_lst)

con.commit()
con.close()
