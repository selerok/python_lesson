day = int(input("enter  the day: "))
month = int(input("enter  the month: "))

if month == 1 and day <= 19 or month == 12 and day >= 22:
    print('capricom')
elif month == 1 and day >= 20 or month == 2 and day <= 18:
    print('aquarius')
elif month == 2 and day >= 19 or month == 3 and day <= 20:
    print('pisces')
elif month == 3 and day >= 21 or month ==4 and day <= 19:
    print('aries')
elif month == 4 and day >= 20 or month ==5 and day <= 20:
    print('taurus')
elif month == 5 and day >= 21 or month == 6 and day <= 20:
    print('gemini')
elif month == 6 and day >= 21 or month == 7 and day <= 22:
     print('cancer')
elif month == 7 and day >= 23 or month == 8 and day <= 22:
    print('leon')
elif month == 8 and day >= 23 or month ==9 and day <= 22:
    print('virgo')
elif month == 9 and day >= 23 or month ==10 and day <= 22:
    print('libra')
elif month == 10 and day >= 23 or month ==11 and day <= 21:
    print('scorpio')
elif month == 11 and day >= 22 or month == 12 and day <= 21:
    print('sagittarius')
else:
    print('не корректный ввод данных')
    print('верный формат даты: от 01 до 31')
    print('верный формат месяца: от 01 до 12')