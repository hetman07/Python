# Города выбранной страны

# Добавьте к предыдущей программе возможность выбора страны. 
# Пусть пользователь должен ввести название страны. 
# Далее выведите все города этой страны и их численность населения.
import pymysql
from config import dbconfig

connection = pymysql.connect(**dbconfig, charset="utf8mb4")

if connection.open:
    print("Connection is succsseful")


with connection.cursor() as cursor:
    cursor.execute("USE world")
    query = "SELECT name FROM country"
    cursor.execute(query)

    for i, name_country in enumerate(cursor.fetchall(), start=1):
        print(f"{i}. {name_country[0]}")

inp_country = input("Enter the name of the coutry for searching: ").capitalize().strip()

with connection.cursor() as cursor:
    cursor.execute("USE world")
    query = """SELECT i.name, i.population
                FROM city i
                WHERE CountryCode in (SELECT c.code 
                                        FROM country c 
                                      WHERE c.name = %s) 
                LIMIT 100
    """
    cursor.execute(query, (inp_country,))
    for name, population in cursor.fetchall():
        print(f"{name} - {population}")
