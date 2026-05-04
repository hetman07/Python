# Генератор уникальных элементов

# Создайте генератор, который принимает список элементов
# и выдаёт только уникальные значения,
# сохраняя порядок их появления в исходном списке.

data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]


def get_unique_list(data):
    unique_list = set()
    for item in data:
        if item not in unique_list:
            yield item
            unique_list.add(item)


print(list(get_unique_list(data)))
