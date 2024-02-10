import csv

def readFile(filename: str) -> list:
    """
    считываем данные из БД
    :param filename:
    :return: list
    """
    with open(filename, "r", encoding='utf8') as file:
        reader = csv.DictReader(file, delimiter=',', quotechar='"')
        students = list(reader)[1:]
    return students

def replace_null(list):
    """Replace the None field with 0

    Keyword arguments:
    list -- List of dictionaries representing students
    """
    for student in list:
        if (student['score'] == 'None'): student['score'] = 0

def insertionSort(list, col):
    """Sort the list using the insertion sorting method

        Keyword arguments:
        list -- List of dictionaries representing students
        col -- Column by which the rows will be compared
      """
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while (j >= 0 and int(temp[col]) < int(list[j][col])):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = temp

def output(students):
    """
    вывод результата

    :param students:
    :return:
    """
    print("10 класс:")
    count = 1
    for student in students[::-1]:
        if "10" in student["class"]:
            print(f"{count} Место: {student['Name'].split(' ')[1]} {student['Name'].split(' ')[0]}")
            count += 1
        if count == 4: break


if __name__ == "__main__":
    students = readFile("students.csv")
    replace_null(students)
    insertionSort(students, "score")
    output(students)