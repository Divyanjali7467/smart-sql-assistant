import sqlite3

connection = sqlite3.connect("database/company.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
    employee_id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER,
    city TEXT
)
""")

employees = [
    (1, "Rahul", "IT", 75000, "Delhi"),
    (2, "Priya", "HR", 50000, "Mumbai"),
    (3, "Ankit", "Finance", 65000, "Pune"),
    (4, "Sneha", "IT", 80000, "Bangalore"),
    (5, "Rohan", "Marketing", 55000, "Lucknow")
]

cursor.executemany(
    "INSERT OR REPLACE INTO employee VALUES (?, ?, ?, ?, ?)",
    employees
)

connection.commit()
connection.close()

print("Database created successfully.")