import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="royal"
)
mycursor = mydb.cursor()

sql = "INSERT INTO students (name, age, gender) VALUES (%s, %s, %s)"
val = ("John", "22", "M")

mycursor.execute(sql, val)

mydb.commit()

mycursor.close()
mydb.close()

