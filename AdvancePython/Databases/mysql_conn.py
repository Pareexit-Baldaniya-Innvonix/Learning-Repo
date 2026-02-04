import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="employee"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS employee")
mycursor.execute("CREATE TABLE IF NOT EXISTS info (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), addr VARCHAR(255))")
mycursor.execute('INSERT INTO info (name, addr) VALUES ("Virat", "India"), ("Rohit", "India"), ("Rachin", "New Zealand")')

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM info")
myresult = mycursor.fetchall()
print(myresult)