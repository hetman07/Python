# Поиск и удаление дубликатов

# Напишите программу, которая удаляет дублирующиеся строки из файла 
# и сохраняет результат в новый файл.

# Имя нового файла формируется как unique_<original_filename>.

# Если файл не существует, программа должна вывести ошибку.

# Исходный порядок строк должен сохраниться.

# Если в файле нет дубликатов, создаётся точная копия файла.

# Используйте файл movies_to_watch.txt.
import os

input_namefile = input("Enter the name of file for searching: ").lower()

base_path = f"{os.getcwd()}/27_File"

inp_file_path = os.path.join(base_path, input_namefile)

unique_lst = []

try:
    with (
        open(inp_file_path, "r", encoding="utf-8") as file,
        open(f"27_File/unique_{input_namefile}", "w", encoding="utf-8") as out_file,
    ):
        for item in file.readlines():
            if item not in unique_lst:
                unique_lst.append(item)
        out_file.writelines(unique_lst)
        print(f"Dublicate was deleted and saved in unique_{input_namefile}")
except FileNotFoundError:
    print(f"{input_namefile} is not found.")
