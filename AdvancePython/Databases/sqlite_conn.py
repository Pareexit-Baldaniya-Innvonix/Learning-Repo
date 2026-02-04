import sqlite3

connection = sqlite3.connect("my_company.db")
cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS employee (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT,
        salary REAL
    )
"""
)

new_employee = (1, "Alice Smith", "Engineering", 75000.0)

cursor.execute("INSERT INTO employee VALUES (?, ?, ?, ?)", new_employee)
connection.commit()

cursor.execute("SELECT * FROM employee")
all_employee = cursor.fetchall()

for row in all_employee:
    print(f"ID: {row[0]}, Name: {row[1]}, Salary: {row[3]}")

connection.close()
