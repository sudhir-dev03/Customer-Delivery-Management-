import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123@Faujdar"
    )

    print("Connected Successfully")

except Exception as e:
    print(e)