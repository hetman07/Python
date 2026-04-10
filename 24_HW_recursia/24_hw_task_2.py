# Сумма вложенных чисел

# Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.

# Данные:

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

# Пример вывода:

# 28
def sum_innerlist(nested_numbers: list, ind = 0):
    if ind == len(nested_numbers):
        return 0
    
    item = nested_numbers[ind]
    
    if isinstance(item, list):
        return sum_innerlist(item) + sum_innerlist(nested_numbers, ind + 1)

    return item + sum_innerlist(nested_numbers, ind + 1)

print(sum_innerlist(nested_numbers))

# с помощью хвостовой рекурсии решение задачи
def sum_innerlist_tail(nested_numbers: list, ind = 0, acc = 0):
    
    if ind == len(nested_numbers):
        return acc
    
    item = nested_numbers[ind]
    
    if isinstance(item, list):
        acc = sum_innerlist_tail(item, 0, acc)
    else:
        acc += item
        
    return sum_innerlist_tail(nested_numbers, ind + 1, acc)

print(sum_innerlist_tail(nested_numbers))

