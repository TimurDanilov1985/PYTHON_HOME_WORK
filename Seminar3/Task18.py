#Задача 18: Требуется найти в массиве A[1..N] самый близкий по
#величине элемент к заданному числу X. Пользователь в первой строке
#вводит натуральное число N – количество элементов в массиве. В
#последующих строках записаны N целых чисел Ai. Последняя строка
#содержит число X
#5
# 2 3 4 5
#6
#-> 5
import random
n = int(input('введите количество элементов в списке:\t'))
x = int(input('Введите число:\t'))
my_list = list()
for i in range(n):
    elem = random.randint(1, 10)
    my_list.append(elem)
print('Вывод списка: ',my_list)
my_list.sort()
print('Вывод отсортированного списка по возрастанию: ',my_list)
my_list1 = set(my_list)
my_list = list(my_list1)
my_list.sort()
n = len(my_list)
print('Список уникальных чисел',my_list)
count = 0
detect = 0
for i in range(n):
    if x > my_list[i]:
        count += 1
    if x == my_list[i]:
        detect = 1
if detect == 1:  
    if x < my_list[n - 1] and x > my_list[0]:
        print(f'Самые близкие по величине элементы к заданному числу {x} равны: {my_list[count - 1]}, {my_list[count + 1]}')
    elif x == my_list[0]:
        print(f'Самый близкий по величине элемент к заданному числу {x} равен: {my_list[1]}')
    elif x == my_list[n - 1]:
        print(f'Самый близкий по величине элемент к заданному числу {x} равен: {my_list[n - 2]}')
elif x < my_list[0]:
    print(f'Самый близкий по велечине элемент к заданному числу {x} равен: {my_list[0]}')
elif x > my_list[n - 1]:
    print(f'Самый близкий по величине элемент к заданному числу {x} равен: {my_list[count - 1]}')
elif detect == 0:
    print(f'Самые близкие по величине элементы к заданному числу {x} равны: {my_list[count - 1]}, {my_list[count]}')