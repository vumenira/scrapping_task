import requests
import bs4
import csv

resource_tsk = requests.get("https://data.uoi.ua/contest/uoi/2024/results")

site_tsk = bs4.BeautifulSoup(resource_tsk.content, "html.parser")

table_head_tsk = site_tsk.select("thead > tr > th")
table_body_tsk = site_tsk.select("tbody > tr")
TABLE_TSK = [[]]

for row in table_head_tsk:
    TABLE_TSK[0].append(row.text)

for row in table_body_tsk:
    row_tsk = []
    for element in row.select("td"):
        row_tsk.append(element.text)
    TABLE_TSK.append(row_tsk)

first = []
second = []
third = []
f, s, t = 1, 1 ,1

for row in TABLE_TSK:

    if row[-1] == "I":
        student = {"#":f, "Ім'я":row[1], "Команда":row[2], "Клас":row[3], "Сума":row[-2]}
        f += 1
        first.append(student)
    elif row[-1] == "II":
        student = {"#": s, "Ім'я": row[1], "Команда": row[2], "Клас": row[3], "Сума": row[-2]}
        s += 1
        second.append(student)
    elif row[-1] == "III":
        student = {"#": t, "Ім'я": row[1], "Команда": row[2], "Клас": row[3], "Сума": row[-2]}
        t += 1
        third.append(student)

with open("first.csv", "w", encoding="utf-8", newline="") as csvfile:
    filenames = ['#', "Ім'я", 'Команда', 'Клас', 'Сума']
    writer = csv.DictWriter(csvfile, fieldnames=filenames)
    writer.writeheader()
    writer.writerows(first)

with open("second.csv", "w", encoding="utf-8", newline="") as csvfile:
    filenames = ['#', "Ім'я", 'Команда', 'Клас', 'Сума']
    writer = csv.DictWriter(csvfile, fieldnames=filenames)
    writer.writeheader()
    writer.writerows(second)

with open("third.csv", "w", encoding="utf-8", newline="") as csvfile:
    filenames = ['#', "Ім'я", 'Команда', 'Клас', 'Сума']
    writer = csv.DictWriter(csvfile, fieldnames=filenames)
    writer.writeheader()
    writer.writerows(third)