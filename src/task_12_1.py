import sqlite3

# Таблица Student section
con = sqlite3.connect('Student_section.db')
cur = con.cursor()
cur.execute('''PRAGMA foreign_keys=on''')
cur.execute('''CREATE TABLE department
               (department_id int  PRIMARY KEY, name text)''')

# Таблица Teacher
cur.execute('''CREATE TABLE teacher(teacher_id int PRIMARY KEY, department_id int,
               first_name text, last_name text, phone_number int,
               FOREIGN KEY(department_id) REFERENCES department(department_id))''')

# Таблица Course
cur.execute('''CREATE TABLE course
               (course_id int PRIMARY KEY, department_id int, title text, other_details text,
               FOREIGN KEY(department_id) REFERENCES department(department_id))''')

# Таблица Section
cur.execute('''CREATE TABLE section
               (section_id int PRIMARY KEY, course_id int, teacher_id int, capacity int,
               FOREIGN KEY(course_id) REFERENCES Course(course_id),
               FOREIGN KEY(teacher_id) REFERENCES Teacher(teacher_id))''')

# Таблица Student
cur.execute('''CREATE TABLE student
               (student_id int PRIMARY KEY, first_name text, last_name text, date_of_birth date)''')

# Таблица Student section
cur.execute('''CREATE TABLE student_section
               (section_id int, student_id int,
               FOREIGN KEY(section_id) REFERENCES student(course_id),
               FOREIGN KEY(student_id) REFERENCES section (teacher_id))''')
cur.execute('''INSERT INTO student_selection VALUES (152, 568)''')

con = sqlite3.connect('Student_section.db')
cur = con.cursor()
for row in cur.execute('SELECT * FROM selection'):
    print(row)
con.commit()
con.close()
