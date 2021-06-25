import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "1813",
    port = 3306
)
cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS academy")