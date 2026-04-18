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


def analyze_course_report():
    try:
        with open(
            "28_JSON_DateTime/54_leeson_28/student_courses.json", "r", encoding="utf-8"
        ) as infile:
            students = json.load(infile)
    except FileNotFoundError:
        print("File is not found.")
        return
    except json.JSONDecodeError:
        print("Invalid JSON format")
        return

    total_students = len(students)

    total_age = 0
    for student in students:
        birth = datetime.strptime(student["birth_date"], "%d.%m.%Y")
        enrollment = datetime.strptime(student["enrollment_date"], "%d.%m.%Y")

        total_age += enrollment.year - birth.year
        if (
            enrollment.month,
            enrollment.day,
        ) < (
            birth.month,
            birth.day,
        ):
            total_age -= 1
    try:
        avg_age = total_age / total_students
    except ZeroDivisionError:
        print("ZeroDivisionError")
        avg_age = 0

    report = {
        "total_students": total_students,
        "average_enrollment_age": avg_age,
    }

    out_filename = f"{os.path.splitext('student_courses.json')[0]}_report.json"

    with open(
        "28_JSON_DateTime/54_leeson_28/" + out_filename, "w", encoding="utf-8"
    ) as outfile:
        json.dump(report, outfile, indent=4)

    return report


print(analyze_course_report())
