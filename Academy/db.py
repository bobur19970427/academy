import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "webshox",
    port = 3306
)
cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS academy")