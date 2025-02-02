# Запрос расходов за каждый день недели
pon = float(input("kakie rashody v ponedelnik?: "))
vtor = float(input("kakie rashody vo vtornik: "))
sred=float(input("kakie rashody v sredu: "))
chet=float(input("kakie rashody v chetverg: "))
pat=float(input("kakie rashody v patnitsu: "))
cub=float(input("kakie rashody v subbotu: "))
voskr=float(input("kakie rashody v voskerenie "))

# Вычисление общей суммы расходов
obshaya_summa_rashodov=pon + vtor + sred + chet + pat + cub +v oskr

# Вычисление среднего расхода в день
sredni_rashod=round(obshaya_summa_rashodov/7 , 1)

# Вывод общей суммы расходов и среднего расхода в день
print("za nedely: ",obshaya_summa_rashodov)
print("za den ", sredni_rashod)