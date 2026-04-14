# Фильтрация по ключевому слову

# Напишите программу, которая ищет в файле все строки, 
# содержащие указанное пользователем слово, и сохраняет их в новый файл.

# Имя нового файла формируется как <keyword>_<original_filename>.

# Если файл не существует, программа должна вывести ошибку.

# Если совпадения не найдены, новый файл не создаётся.

# Используйте файл system_log.txt.
import os

keyword = input("Input keyword for searching: ").lower()
original_filename = input(
    "Input the name of file for searching: "
).lower()  # "system_log.txt"

base_path = f"{os.getcwd()}/27_File"

file_path = os.path.join(base_path, original_filename)

match_lists = []

try:
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file.readlines():
            if keyword in line.lower():
                match_lists.append(line)
    if len(match_lists) > 0:
        out_filename = f"{keyword}_{original_filename}"
        out_path = os.path.join(base_path, out_filename)

        with open(out_path, "w", encoding="utf-8") as out_file:
            out_file.writelines(match_lists)
        print(
            f"The strings, that consist '{keyword}', was saved in  {keyword}_{original_filename}"
        )
    else:
        print("No matches.")

except FileNotFoundError:
    print("File is not found.")
