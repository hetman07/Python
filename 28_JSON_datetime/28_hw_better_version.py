# Анализ курсов студентов
# Реализовать программу, которая должна:
# Прочитать файл student_courses.json, содержащий:
# имя,
# дату рождения (birth_date) в формате дд.мм.гггг,
# дату поступления (enrollment_date) в том же формате,
# список курсов.
# Вычислить:
# Общее количество студентов.
# Средний возраст на момент поступления.
# Сохранить отчёт в JSON-файл student_courses_report.json.
import json
import os
from datetime import datetime

BASE_PATH = "28_JSON_DateTime/54_leeson_28/"
filename = BASE_PATH + "student_courses.json"

out_filename = f"{BASE_PATH}{os.path.splitext('student_courses.json')[0]}_report.json"

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as infile:
        return json.load(infile)
    

def save_file(outfilename, report):
    with open(outfilename, "w", encoding="utf-8") as outfile:
        json.dump(report, outfile, indent=4)    

def get_age(birth_date, enroll_date):
    birth = datetime.strptime(birth_date, "%d.%m.%Y")
    enroll = datetime.strptime(enroll_date, "%d.%m.%Y")

    age = enroll.year - birth.year
    
    if (enroll.month, enroll.day,) < (birth.month, birth.day):
        age -= 1
        
    return age

def make_report(students):
    ages = [get_age(s["birth_date"], s["enrollment_date"]) for s in students]
    
    return {
        "total_students": len(students),
        "average_enrollment_age": round(sum(ages) / len(ages), 1),
    }

 
students = read_file(filename)
report = make_report(students)
save_file(out_filename, report)

