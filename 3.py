import csv

def readFile(filename: str) -> list:
    """
    считываем данные из БД
    :param filename:
    :return: list
    """
    with open(filename, "r", encoding='utf8') as file:
        reader = csv.DictReader(file, delimiter=',', quotechar='"')
        students = list(reader)
    return students

def search(students, element):
    """
    Линейный поиск в БД

    :param students:
    :param element:
    :return:
    """
    for i in range(len(students)):
        if element == students[i]["titleProject_id"]:
            print(f"Проект № {element} делал: {students[i]['Name'].split(' ')[1]} {students[i]['Name'].split(' ')[0]} он(а) получил(а) оценку - {students[i]['score']}")
            return
    print("Ничего не найдено")


if __name__ == "__main__":
    students = readFile("students.csv")
    text = ''
    while text != "СТОП":
        text = input()
        search(students, text)
