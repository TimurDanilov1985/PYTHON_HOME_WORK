#Задача 28: Напишите рекурсивную функцию sum(a, b),
#возвращающую сумму двух целых неотрицательных чисел. Из
#всех арифметических операций допускаются только +1 и -1.
#Также нельзя использовать циклы.
#2 2
#4
def Input():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    return (a, b)
def Summa(a, b):
    if a == 0:
        return b
    else:
        return Summa(a - 1, b + 1)
def Output(r):
    print('Сумма чисел равна: ', r)
(number1, number2) = Input()
result = Summa(number1, number2)
Output(result)