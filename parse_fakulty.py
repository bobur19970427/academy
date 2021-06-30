import requests
from bs4 import BeautifulSoup
import mysql.connector


link = f'https://jspi.uz/institut/fakultetlar/'

product = []

lal = requests.get(link).text
soup = BeautifulSoup(lal, 'lxml')
# block = soup.find('div', class_='menu-fakvakaf-container')
ul = soup.find('ul', id='fakvakaf_menu')
fak = ul.find_all('li', class_='menu-item-has-children')
for fak_nomi in fak:
    fak_nomi = fak_nomi.find('a').text
    a = (fak_nomi, 'yusupov')
    product.append(a)

db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1813",
        database='academy1'
    )
mycursor = db.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS fakultet2 (id INT(50) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), dek VARCHAR(255))")
sql = "INSERT INTO fakultet2 (name, dek) VALUES (%s,%s)"
mycursor.executemany(sql, product)
db.commit()
