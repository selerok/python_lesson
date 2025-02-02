mon=float(input("enter tne monday's price: "))
tue=float(input("enter the tuesday's price: "))
wednesday=float(input("enter the wednesday's price: "))
thursday=float(input("enter the thursday's price: " ))
friday=float(input("enter the friday's price" ))
saturday=float(input("enter the tsatuday's price: " ))
sunday=float(input("enter the sunday's price: " ))

summa=monday+tuesday+wednesday+thursday+friday+saturday+sunday
print(f'общая сумма: {summa}')


average=summa/7
average_round=round(average,1)
print(f'среднее арифмитическое: {average_round}')