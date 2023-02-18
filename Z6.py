# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

a = input(str("Введите шестизначный номер билета: "))
if int(a) > 99999 and int(a) <1000000:
    if int(a[0]) + int(a[1]) + int(a[2]) == int(a[3]) + int(a[4]) + int(a[5]):
        print(f'Билет с номером {a} является счастливым')
    else:
        print(f'Билет с номером {a} не является счастливым')
else:
    print(f'Число {a} не является шестизначным, попробуйте еще раз')