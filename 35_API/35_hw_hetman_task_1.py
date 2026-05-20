#Предсказание пола по имени

# Изучите документацию API предсказания пола по имени: genderize.io/documentation. 
# Напишите программу, которая запрашивает имя пользователя и выводит его 
# пол и вероятность этого предсказания.

import requests

inp_name = input("Enter the kinder of name: ").lower()

BASE_URL = "https://api.genderize.io"

params = {"name": inp_name}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()

    print(f"Probability gender: {data['gender']}")
    print(f"Probability: {data['probability'] * 100:.1f}%")
else:
    print("API is not avilable.")
