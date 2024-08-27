import sqlite3
with sqlite3.connect('users.db') as connection:
    cursor=connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    salary INTEGER NOT NULL
    )''')
    cursor.execute('''SELECT * FROM employees''')
    for row in cursor.fetchall():
        print(row)