# 2. Сумма вложенных чисел
# Напишите функцию, которая принимает список словарей,
# где каждый словарь содержит имя пользователя и список баллов.
# Функция должна вернуть сумму всех чисел. Добавьте документацию и
# аннотации типов для всех параметров и возвращаемого значения.
# Пример вывода:

# Итоговый балл: 156
# Данные:
from functools import reduce
from typing import TypedDict

class User(TypedDict):
    name: str
    scores: list[int]
    
data: list[User] = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]},
]

def sum_score(data_lst: list[User]) -> int:
    """
    Calculates the total sum of all scores using reduce.

    Args:
        data_lst (list[dict[str, Union[str, list[int]]]]): A list of dictionaries where each
            dictionary contains:
                - "name" (str): The user's name
                - "scores" (list[int]): A list of integer scores

    Returns:
        int: The total sum of all scores.
    """
    items = map(lambda item: item['scores'], data_lst)
    sum_item = map(sum, items)
    result = sum(sum_item)

    return result

print(sum_score(data))

def sum_score_reduce(data_lst: list[User]) -> int:
    """
    Calculates the total sum of all scores using reduce.

    Args:
        data_lst [list[User]]: A list of dictionaries where each
            dictionary contains:
                - "name" (str): The user's name
                - "scores" (list[int]): A list of integer scores

    Returns:
        int: The total sum of all scores.
    """
    scores = reduce(
    lambda acc, user: acc + sum(user["scores"]),
    data_lst,
    0
)
    return scores
print(sum_score_reduce(data))