import sqlite3
with sqlite3.connect('users.db') as connection:
    cursor=connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    salary INTEGER NOT NULL
    )''')
    cursor.execute('''INSERT INTO employees(name, salary)
        VALUES ('tema',20000), ('azret', 1500),('danya', 2000), ('elmir',3000), ('elmirza',4000),('emir',6000),('ela',7000),('vasya',8000), ('dima',9000), ('akilbek', 10000)''')
    cursor.execute('''SELECT * FROM employees''')
    for row in cursor.fetchall():
        print(row)