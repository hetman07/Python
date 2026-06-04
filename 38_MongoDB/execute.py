# Добавление товаров

# Создайте программу, которая подключается к MongoDB и:

# выбирает базу ich_edit и коллекцию products_<your_group>_<your_full_name>
#   очищает коллекцию перед началом
#   добавляет 3 товара с полями: name, price, stock
#   выводит сообщение о количестве добавленных товаров
# Увеличение цен

# Продолжите предыдущую задачу. Теперь программа должна:
#   увеличить цену всех товаров на 20%
#   вывести количество обновлённых записей
#   затем вывести список всех товаров с новыми ценами

from pymongo import MongoClient
from config import mongo
from items import items

def run_hw():
    try:
        with MongoClient(mongo) as client:
            client.admin.command("ping")
            print("Connection successful!")

            db = client["ich_edit"]
            products = db["products_dam281125_hetman"]

            products.delete_many({})

            result = products.insert_many(items)
            print(f"{len(result.inserted_ids)} products inserted.")

            res_update = products.update_many({}, {"$mul": {"price": 1.2}})
            print(f"Prices updated for {res_update.modified_count} products.")

            docs = products.find()
            print("Updated products:")
            for doc in docs:
                print(f"- {doc['name']} - ${doc['price']:.2f}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    run_hw()
