#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
#повторениями). Выдать без повторений в порядке возрастания все те числа, которые
#встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
#элементов второго множества. Затем пользователь вводит сами элементы множеств.
#11 6
#2 4 6 8 10 12 10 8 6 4 2
#3 6 9 12 15 18
#6 12
#import random
n = int(input('Введите количество элементов первого списка:\t'))
m = int(input('Введите количество элементов второго списка:\t'))
print(f'Введите {n} чисел в качестве элементов первого списка через пробел')
list_1 = list(map(int,input().split()))
print()
print('Введен первый список чисел: ', list_1)
print()
print(f'Введите {m} чисел в качестве элементов второго списка через пробел')
list_2 = list(map(int,input().split()))
print()
print('Введен второй список чисел: ', list_2)
print()
list_1 = set(list_1)
list_2 = set(list_2)
list_1 = list(list_1)
list_2 = list(list_2)
print('Вывдод первого списка с уникальными числами: ', list_1)
print('Вывод второго списка с уникалными числами: ', list_2)
list_3 = []
n = len(list_1)
m = len(list_2)
if n >= m:
    for i in range(m):
        for j in range(n):
           if list_2[i] == list_1[j]:
               list_3.append(list_1[j])
elif n <= m:
    for i in range(n):
        for j in range(m):
           if list_1[i] == list_2[j]:
               list_3.append(list_1[j])
list_3.sort()
print('Вывод в порядке возрастания чисел без повторений, встречающихся в обоих наборах: ', list_3)