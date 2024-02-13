import sqlite3

# Connect to the SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the employees table



conn.close()

print("Data inserted successfully.")
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    salary REAL
                )''')

# Insert some data into the employees table
employees_data = [
    ('John Doe', 50000),
    ('Jane Smith', 60000),
    ('Alice Johnson', 55000)
]

cursor.executemany('INSERT INTO employees (name, salary) VALUES (?, ?)', employees_data)

# Commit the changes and close the connection
conn.commit()
conn.close()
print("done")