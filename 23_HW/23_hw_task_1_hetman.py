# Объединение данных в строку
# Напишите функцию, которая принимает список любых данных (строки, числа, списки, словари) 
# и возвращает их строковое представление, объединённое через " | ". 
# Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.
# Пример вывода:
# 42 | hello | [1, 2, 3] | {'a': 1, 'b': 2}
# Данные:
from typing import Any

data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]


def join_elements(data_lst: list[Any]) -> str:
    """
    Converts a list of mixed data types into a single string.

    Each element is converted to a string and joined using " | " as a separator.

    Args:
        data_lst (list[Any]): A list containing elements of any type.

    Returns:
        str: A string with all elements joined by " | ".
    """
    return " | ".join(map(str, data_lst))


print(join_elements(data))
help(join_elements)