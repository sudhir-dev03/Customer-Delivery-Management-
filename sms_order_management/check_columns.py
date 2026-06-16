import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123@Faujdar",
    database="seafood_db"
)

cursor = conn.cursor()

cursor.execute("DESC orders")

for row in cursor.fetchall():
    print(row)

conn.close()