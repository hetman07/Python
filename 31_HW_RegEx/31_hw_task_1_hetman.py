import re
from datetime import datetime

text = """
Meeting on 2024-05-10 or 10/05/2024 at 14:30,
12.05.2016, 22-07-1984, 37.13.1988,
31.02.2020, 01.2.2020, 9-9-1999
"""
pattern = r"\b(0?[1-9]|[12][0-9]|3[01])([./-])(0?[1-9]|1[0-2])\2(\d{4})\b"

date_from_text = re.findall(
    r"\b(\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}|\d{2}\.\d{2}\.\d{4})\b", text
)
print("version 1: ", date_from_text)

# improve version

valid_dates = []

for match in re.finditer(pattern, text):
    date_str = match.group(0)
    sep = match.group(2)

    try:
        # validate real calendar date
        datetime.strptime(date_str, f"%d{sep}%m{sep}%Y")
        valid_dates.append(date_str)
    except ValueError:
        continue

print("best version: ", valid_dates)
