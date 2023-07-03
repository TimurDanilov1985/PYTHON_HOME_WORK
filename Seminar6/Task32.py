#Задача 32: Определить индексы элементов массива (списка),
#значения которых принадлежат заданному диапазону (т.е. не
#меньше заданного минимума и не больше заданного
#максимума)
#Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#Вывод: [1, 9, 13, 14, 19]
import random
def Input():
    list_1 = [random.randint(-100, 100) for i in range(random.randint(10, 20))]
    print('Введите диапазон в пределах которого будут определены индексы')
    min_val = int(input('Введите минимальное значение: '))
    max_val = int(input('Введите максимальное значение: '))
    return (list_1, min_val, max_val)
def Index(lis, mini, maxi):
    list_i = list()
    for i in range(len(lis)):
        if lis[i] > mini and lis[i] < maxi:
            list_i.append(i)
    return list_i
def Output(result, lis1):
    print('Заданный список: ', lis1)
    print('Индексы элементов в заданном диапазоне: ', result)
(list_1, min_val, max_val) = Input()
list_result = Index(list_1, min_val, max_val)
Output(list_result, list_1)