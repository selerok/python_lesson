#Ввод данных
print("Zodiac Sign Calculation Program" + "\n")
print("ВНИМАЕНИЕ ВВОДИТЕ ДАННЫЕ КОРРЕКТНО!!!" + "\n")
day = int(input("введите корректную дату в формате от 01 до 31: "))
month = int(input("введите корретный месяц в формате от 01 до 12: "))

# Создание таблицы
aries = (month == 3 and day >= 21 or month ==4 and day <= 19)

if aries:
    print("Oven")
elif