# Task 2:
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

try:
    conn = mysql.connector.connect(
        user=db_user, host=db_host, passwd=db_pass, database=db_name
    )

    if conn.is_connected():
        print(f"Successfully connected with '{db_name}' database!")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if "conn" in locals() and conn.is_connected():
        conn.close

# cursor = conn.cursor()

# records = """CREATE TABLE EMPLOYEE(
# NAME CHAR(20) NOT NULL,
# AGE INT,
# CITY CHAR(30)
# )"""

# cursor.execute(records)
# conn.close()
