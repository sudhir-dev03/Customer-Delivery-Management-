import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123@Faujdar",
    database="seafood_db"
)

cursor = conn.cursor()

cursor.execute("""
ALTER TABLE orders
ADD COLUMN driver_name VARCHAR(100)
""")

conn.commit()

print("Column Added Successfully")

conn.close()