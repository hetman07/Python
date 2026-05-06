# Разделение списка тегов

# Реализуйте программу, которая должна:

# Прочитать строку с тегами, введёнными пользователем.

# Разделить её на отдельные теги, независимо от того, чем они были разделены (запятые, точки с запятой, слэши или пробелы).

# Удалить лишние пробелы и пустые значения.
import re

tag_input = " python, data-science / maschine-learning; AI neural-networks "
pattern = r"[,\s/;]+"

# version 1
clean_text = re.sub(pattern, ",", tag_input).split(",")
result_one = [item_ for item_ in clean_text if item_]
print("result_one: ", result_one)

# version 2
tags = re.split(pattern, tag_input)
result_two = [tag for tag in tags if tag]
print("result_two: ", result_two)
