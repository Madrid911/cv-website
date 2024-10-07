import sqlite3

# Create a new SQLite database (or connect to it if it exists)
connection = sqlite3.connect('database/cv_website.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS personal_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    bio TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS education (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    degree TEXT NOT NULL,
    institution TEXT NOT NULL,
    year_completed INTEGER NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS work_experience (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_title TEXT NOT NULL,
    company TEXT NOT NULL,
    year_started INTEGER NOT NULL,
    year_ended INTEGER NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT NOT NULL,
    description TEXT NOT NULL
);
''')

# Insert sample data (optional)
cursor.execute("INSERT INTO personal_info (name, bio) VALUES (?, ?)", ("Mosehlane Lekgau", "A passionate web developer."))

# Commit the changes and close the connection
connection.commit()
connection.close()
