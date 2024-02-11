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

def genHash(s: str):
    alphabet = ''.join(chr(i) for i in range(1040, 1103 + 1)) + "ёЁ "
    d = {letters: i for i, letters in enumerate(alphabet,1)}
    p = 67
    m = 10**9 + 9
    hash_val = 0
    p_pow = 1
    for c in s:
        hash_val = (hash_val + d[c] * p_pow) % m
        p_pow = (p_pow * p) % m

    return int(hash_val)

def writeFile(filename, data) -> None:
    """
    записываем данные в БД

    :param filename: название файла
    :param data: данные для записи
    :return: None
    """
    with open(filename, "w", encoding="utf8", newline='') as file:
        keys = ["id","Name","titleProject_id","class","score"]
        writer = csv.DictWriter(file, fieldnames=keys, delimiter=",")
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    students = readFile("students.csv")
    students_with_hash = []
    for row in students:
        row["id"] = genHash(row['Name'])
        students_with_hash.append(row)
    writeFile("students_with_hash.csv", students_with_hash)