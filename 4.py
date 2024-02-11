import csv, random, string

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

def genPassword():
    """
    Генерируем пароль для пользователя

    :return:
    """
    character = string.ascii_letters + string.digits
    passwd = ''.join(random.choice(character) for _ in range(0,8))
    return passwd

def genLogin(student):
    """
    Генерируем логин для пользователя

    :param student:
    :return:
    """
    name = student["Name"].split(' ')
    login = f"{name[0]}_{name[1][0]}{name[2][0]}"
    return login

def writeFile(filename, data) -> None:
    """
    записываем данные в БД

    :param filename: название файла
    :param data: данные для записи
    :return: None
    """
    with open(filename, "w", encoding="utf8", newline='') as file:
        keys = ["id","Name","titleProject_id","class","score", "login", "password"]
        writer = csv.DictWriter(file, fieldnames=keys, delimiter=",")
        writer.writeheader()
        for student in data:
            student["login"] = genLogin(student)
            student['password'] = genPassword()
            writer.writerow(student)



if __name__ == "__main__":
    students = readFile("students.csv")
    writeFile("students_password.csv", students)
