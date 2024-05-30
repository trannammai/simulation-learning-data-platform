import random
from faker import Faker
import mysql.connector

# Create a Faker instance
fake = Faker()

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

cursor = db.cursor()

# Insert data into tbl_school and tbl_course
for _ in range(10):
    cursor.execute("INSERT INTO tbl_school (name) VALUES (%s)", (fake.company(),))
    if _ < 3:
        cursor.execute("INSERT INTO tbl_course (name) VALUES (%s)", (fake.job(),))

# Get school and course IDs
cursor.execute("SELECT id FROM tbl_school")
school_ids = [row[0] for row in cursor.fetchall()]
cursor.execute("SELECT id FROM tbl_course")
course_ids = [row[0] for row in cursor.fetchall()]

# Insert data into tbl_student
for _ in range(1000):
    cursor.execute(
        "INSERT INTO tbl_student (name, schoolId, courseId) VALUES (%s, %s, %s)",
        (fake.name(), random.choice(school_ids), random.choice(course_ids))
    )

db.commit()