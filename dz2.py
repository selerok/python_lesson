# Запрос дня и месяца рождения у пользователя
day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения: "))





23
# Проверка корректности введенной даты
valid_date = True
if month < 1 or month > 12 or day < 1:
    valid_date = False
elif month == 2:
    if day > 29:
        valid_date = False
    elif day == 29 and (day % 4 != 0 or (day % 100 == 0 and day % 400 != 0)):
        valid_date = False
elif month in {4, 6, 9, 11}:
    if day > 30:
        valid_date = False
else:
    if day > 31:
        valid_date = False

if not valid_date:
    print("Введите корректную дату в соответствии с календарем.
else:
    # Определение знака зодиака с использованием упрощенной таблицы
    if (month == 1 and day <= 19) or (month == 12 and day >= 22):
        zodiac_sign = "Козерог"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        zodiac_sign = "Водолей"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        zodiac_sign = "Рыбы"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        zodiac_sign = "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        zodiac_sign = "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        zodiac_sign = "Близнецы"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        zodiac_sign = "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        zodiac_sign = "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        zodiac_sign = "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        zodiac_sign = "Весы"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        zodiac_sign = "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        zodiac_sign = "Стрелец"

    print(f"Ваш знак зодиака: {zodiac_sign}")
