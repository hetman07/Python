# Поиск стран

# Напишите программу, которая:
# Парсит таблицу с сайта https://www.iban.com/country-codes и сохраняет 
# ее в подходящей структуре данных;

# Запрашивает у пользователя код страны (пользователь может ввести 
# двухбуквенный или трехбуквенный код) и выводит название страны, 
# соответствующей этому коду.

import requests
import bs4

url = "https://www.iban.com/country-codes"
BASE_PATH = "36_Parser"

text = requests.get(url).text
soup = bs4.BeautifulSoup(text, "lxml")

table_headers = soup.select('th[class="head"]')
headers = [head.text for head in table_headers]
print("headers: ", headers)

column_data = soup.select("table > tbody > tr")
countries = {}

for row in column_data:
    row_data = row.select("td")

    individual_row = [cell.text.strip() for cell in row_data]

    country_name = individual_row[0]
    code_2 = individual_row[1]
    code_3 = individual_row[2]

    countries[code_2] = country_name
    countries[code_3] = country_name

inp_code = input("Input the code (2 or 3 letters) for searching: ").upper()

print(countries.get(inp_code))
