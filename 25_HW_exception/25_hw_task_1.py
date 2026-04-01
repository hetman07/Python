# Деление без ошибок
# Напишите функцию, которая выполняет деление двух чисел,
# введенных пользователем, и обрабатывает возможные ошибки.

# Пример вывода:

# Введите делимое: 345

# Введите делитель: 5a

# Ошибка: Введено некорректное число.


def division_nums(num: int, divisor: int):
    try:
        num_1 = int(num)
    except ValueError:
        raise ValueError("Invalid number (num).")

    try:
        divisor_1 = int(divisor)
    except ValueError:
        raise ValueError("Invalid number (divisor)")

    if divisor_1 == 0:
        raise ZeroDivisionError("Division by zero is not allowed")

    return round(num_1 / divisor_1)


num = input("Enter dividend: ")
divisor = input("Enter divisor: ")

try:
    print(division_nums(num, divisor))
except ValueError as err:
    print(err)
except ZeroDivisionError as e:
    print(e)
