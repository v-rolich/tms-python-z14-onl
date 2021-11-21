import sqlite3

con = sqlite3.connect('MyDB.db')

cur = con.cursor()

for row in cur.execute('SELECT * FROM Department d join Course c on d.id = c.department\n'
                       'join Teacher t on d.id = t.department'
                       ' Where c.title=:name', {'name': 'Python'}):
    print(row)
