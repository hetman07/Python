# Сумма цифр числа
# Напишите рекурсивную функцию, которая находит сумму всех цифр числа.
# Данные:
# num = 43197
# Пример вывода:
# 24

def sum_of_digits(n: int):
    
    if n <= 9:
        return n
    
    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(43197))



