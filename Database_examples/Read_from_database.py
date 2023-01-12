import sqlite3

conn = sqlite3.connect("student.sqlite")
cursor = conn.cursor()

select_students = """ 
SELECT id, firstname, lastname 
FROM students 
WHERE age >= 15 
"""

cursor.execute(select_students)
first_student = cursor.fetchone()
more_students = cursor.fetchmany(10)
other_students = cursor.fetchall()

student_j = """
SELECT substr(firstname, 0, 1)
FROM students

"""
student_j = cursor.fetchone()
print(student_j)

average_query = """ 
SELECT avg(age) 
FROM students 
WHERE gender = ? 
"""
average_age = cursor.execute(average_query, ('female',)).fetchone()[0]

group_by_query = """ 
SELECT gender, sum(age)
FROM students 
GROUP BY gender 
"""
age_by_gender = cursor.execute(group_by_query).fetchall()
