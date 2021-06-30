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
s=0
for fak_nomi in fak:
    yu = fak_nomi.find('ul', class_='sub-menu')
    yun = yu.find_all('li', class_='menu-item-object-page')
    # print(yun)
    s+=1
    for yunalish in yun:
        yu_nomi = yunalish.find('a').text
        a = (yu_nomi,s)
        product.append(a)
print(product)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1813",
    database='academy1'
)
mycursor = db.cursor()
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS yunalish (id INT(50) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fak_id INT(50))")
sql = "INSERT INTO yunalish (name, fak_id) VALUES (%s,%s)"
mycursor.executemany(sql, product)
db.commit()
