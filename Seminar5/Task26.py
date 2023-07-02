#Задача 26: Напишите программу, которая на вход принимает
#два числа A и B, и возводит число А в целую степень B с
#помощью рекурсии.
#A = 3; B = 5 -> 243 (3⁵)
#A = 2; B = 3 -> 8
def Degree(a, b):
    if b == 0:
        return 1
    else:
        return a * Degree(a, b - 1)
def Input():
    a = int(input('Введите число для возведения в степень: '))
    b = int(input('Введите степень: '))
    return (a, b)
def Output(r, a, b):
    print(f'Число {a} в степени {b} равно: {r}')
(number, deg) = Input()
result = Degree(number, deg)
Output(result, number, deg)