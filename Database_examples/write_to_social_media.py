import sqlite3

conn = sqlite3.connect("sm_app.sqlite")
cursor = conn.cursor()

write_to_users = """
INSERT INTO
    users(name, age, gender, nationality)
VALUES 
    ('James', 25, 'male', 'USA'),
    ('Leila', 32, 'female', 'France'),
    ('Brigitte', 35, 'female', 'England'),
    ('Mike', 40, 'male', 'Denmark'),
    ('Elizabeth', 21, 'female', 'Canada');

"""

cursor.execute(write_to_users)
conn.commit()
