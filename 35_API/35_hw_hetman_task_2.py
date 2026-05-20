# 2. Получение биржевых данных через APIНапишите программу, которая запрашивает у пользователя 
#     тикер (symbol) акций, 
#     обращается к функции с помесячными данными 
# о результатах торгов (TIME_SERIES_MONTHLY) в API ресурса www.alphavantage.co, 
#     запрашивает результат в формате csv, записывает его в файл. 
    
# Доступность ресурса предварительно нужно проверить. 

# После этого файл требуется 
#     прочитать, 
#     извлечь данные из столбца volume и 
#     вычислить среднее значение этого столбца.

import requests
import csv
import statistics

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey=demo'
BASE_PATH = "35_API"

BASE_URL = "https://www.alphavantage.co/query"
symbol = input("Enter the symbol(action): ").upper()

params = {
    "function": "TIME_SERIES_MONTHLY",
    "symbol": symbol,
    "apikey": "QPXQ8IJWOAC68L23",
    "datatype": "csv",
}
r = requests.get(BASE_URL, params=params)

if r.status_code == 200:
    with open(f"{BASE_PATH}/{symbol}.csv", "w", encoding="utf-8", newline="") as f:
        f.write(r.text)

    print("The file was saved successfully.")
else:
    print("API is unavailable.")


def count_statistic_data(volumes):
    return {"avg": round(statistics.mean(volumes), 2)}


volumes = []

with open(f"{BASE_PATH}/{symbol}.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        volumes.append(int(row["volume"]))

if volumes:
    result = count_statistic_data(volumes)
else:
    print("No data")

print("The average amount of : ", result["avg"])
