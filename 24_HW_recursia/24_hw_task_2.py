# Сумма вложенных чисел

# Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.

# Данные:

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

# Пример вывода:

# 28
def sum_innerlist(nested_numbers: list):
    total = 0 
    for item in nested_numbers:
        if isinstance(item, list):
            total += sum_innerlist(item)
        elif isinstance(item, int):
            total += item
    return total

print(sum_innerlist(nested_numbers))
