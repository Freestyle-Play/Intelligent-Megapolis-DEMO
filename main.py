f = open("students.csv", encoding='utf8')
id, name, titleProject_id, class_number, score = f.readline().split(",")

print(id, name, titleProject_id, class_number, score)
table = [] # создаём таблицу.
sum_score = 0
count_score = 0
for text in f:
    # print(text)
    id, name, titleProject_id, class_number, score = text.strip().split(",")
    if score == "None":
        score = 0
    else:
        sum_score += int(score)
        count_score += 1
    table.append([id, name, titleProject_id, class_number, score])
    if 'Хадаров Владимир' in name:
        print(f"Ты получил: {score}, за проект - {id}")

avr_score = round(sum_score/count_score, 3)

print(avr_score)
print(table)