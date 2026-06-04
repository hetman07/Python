# Список всех стран

# Используя базу данных world, выведите названия всех стран 
# из таблицы country. 
# Каждое название должно отображаться с новой строки и 
# номер.
import pymysql
from config import dbconfig

connection = pymysql.connect(**dbconfig, charset='utf8mb4')

if connection.open:
    print("Connection is succsseful")


with connection.cursor() as cursor:
    cursor.execute('USE world')
    query = 'SELECT name FROM country'
    cursor.execute(query)
    
    for i, name_country in enumerate(cursor.fetchall(), start=1):
        print(f'{i}. {name_country[0]}')
        
connection.close()
