import csv

def readFile(filename: str) -> list:
    """
    считываем данные из БД
    :param filename:
    :return students:
    """
    with open(filename, "r", encoding='utf8') as file:
        reader = csv.DictReader(file, delimiter=',')
        students = list(reader)[1:]

        # analog
        # students = []
        #
        # for student in reader:
        #     students.append({"id": student["id"],
        #                      "name": student['Name'],
        #                      "porject_id": student["titleProject_id"],
        #                      "class": student["class"],
        #                      "score": student["score"]})

    return students

def vladimir(students):
    """
    выводит строку с оценкой Владимира и его id проекта

    :param students:
    :return:
    """
    for row in students:
        if "Хадаров Владимир" in row.get("Name"):
            print(f"Ты получил: {row.get('score')}, за проект - {row.get('titleProject_id')}")

def average(students):
    """
    вычисляем среднее число по классу и заменяет ошибочное значение на среднее

    :param students:
    :return:
    """
    count = {}
    sum = {}
    for student in students:
        if student["score"] != "None":
            if student["class"] in count:
                count[student["class"]] += 1
                sum[student["class"]] += int(student["score"])
            else:
                count[student["class"]] = 1
                sum[student["class"]] = int(student["score"])

    for i in range(0, len(students)):
        table = []
        if students[i]["score"] == "None":
            students[i]["score"] = round(sum[students[i]["class"]]/ count[students[i]["class"]], 3)

    return students

def writeFile(filename, data):
    with open(filename, "w", encoding="utf8", newline='') as file:
        keys = ["id","Name","titleProject_id","class","score"]
        writer = csv.DictWriter(file, fieldnames=keys, delimiter=",")
        writer.writeheader()
        writer.writerows(students)

if __name__ == "__main__":
    students = readFile("students.csv")
    vladimir(students)
    students = average(students)
    writeFile("students_new.csv", students)


