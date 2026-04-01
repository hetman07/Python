# Логирование ошибок
# Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log в соответствии с форматом ниже.

# Пример вывода:
# 2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число.
import logging

logging.basicConfig(
    filename="errors.log",
    format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d -  - %(message)s",
    level=logging.ERROR,
)


def division_nums(num: int, divisor: int):
    try:
        num_1 = int(num)
    except ValueError:
        logging.error("Calculation failure! Invalid number (num).")
        raise ValueError("Invalid number (num).")

    try:
        divisor_1 = int(divisor)
    except ValueError:
        logging.error("Calculation failure! Invalid number (divisor).")
        raise ValueError("Invalid number (divisor)")

    if divisor_1 == 0:
        logging.error("Calculation failure! Division by zero is not allowed.")
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
