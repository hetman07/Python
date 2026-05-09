# На лекции при выполнении практического задания 2 
# был получен файл grades.csv. Напишите программу, которая:

# Читает этот файл.

# Создает на его основе три новых файла: grades-Science.csv, 
# grades-Math.csv, grades-Physics.csv. 
# В каждом из этих файлов только два столбца - 
# имя и количество баллов по тому предмету, 
# который указан в названии файла.

# Создает четвертый файл grades-info.csv. 
# В этом файле три строки (по названиям предметов) и 
# столбцы со статистическими характеристиками оценок: 
#     среднее арифметическое, 
#     минимум, 
#     максимум, 
#     медиана, 
#     стандартное отклонение.
    
import csv
import statistics

SUBJECT = ['Science', 'Math','Physics']
BASE_PATH = "29_CSV_statistic"

buckets = {s: [] for s in SUBJECT}

def count_statistic_data(grades):
    return {
    "avg": round(statistics.mean(grades),2),
    "min": min(grades),
    "max": max(grades),
    "median": statistics.median(grades),
    "stdev": round(statistics.stdev(grades),2)
    }

with open(f'{BASE_PATH}/grades.csv', encoding='utf-8-sig') as inp_file:
        reader = csv.DictReader(inp_file)
        for item in reader:
            if item['subject'] in buckets:
                buckets[item['subject']].append((item['name'], int(item['grade'])))
stats_rows = []
                
for subject, rows in buckets.items():
    with open(f"{BASE_PATH}/grades-{subject}.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f) 
        writer.writerow(["name", "grade"])
        writer.writerows(rows)
        # csv.writer(f).writerows([["name", "grade"]] + rows) версия преподавателя короче код

    grades = [grade for _, grade in rows] #оставим только оценки
    stats_rows.append({"subject": subject, **count_statistic_data(grades)})

fields = ["subject", "avg", "min", "max", "median", "stdev"]   

with open(f"{BASE_PATH}/grades-info.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames = fields)
    writer.writeheader()
    writer.writerows(stats_rows)    
