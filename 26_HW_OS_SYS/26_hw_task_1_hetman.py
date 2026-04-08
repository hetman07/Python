# Список файлов и папок

# Напишите программу, которая принимает путь к директории через аргумент командной строки и выводит:
# Отдельно список папок
# Отдельно список файлов

# Пример запуска

# python script.py /home/user/documents
# Пример вывода

# Содержимое директории '/home/user/documents':

# Папки:

# - folder1
# - folder2

# Файлы:

# - file1.txt
# - file2.txt
# - notes.docx
import os
import sys

folders = []
files = []

print("***", sys.argv)
if len(sys.argv) != 2:
    print("Argumen is not found")
    sys.exit(1)

directory = sys.argv[1]

if not os.path.isdir(directory):
    print(f"Directory {directory} is not exists.")
    sys.exit(1)
else:
    print(f"Contents of the directory: {directory}")
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)

        if os.path.isfile(full_path):
            files.append(item)
        elif os.path.isdir(full_path):
            folders.append(item)

print("FOLDERS: ")
for folder in folders:
    print(f" - {folder}")
print("FILES: ")
for file in files:
    print(f" - {file}")

