#Задача 16: Требуется вычислить, сколько раз встречается некоторое
#число X в массиве A[1..N]. Пользователь в первой строке вводит
#натуральное число N – количество элементов в массиве. В последующих
#строках записаны N целых чисел Ai. Последняя строка содержит число X
#5
#1 2 3 4 5
#3
#-> 1
import random
n = int(input('Введите количество элементов в списке:\t'))
x = int(input('Введите некоторое число:\t'))
my_list = [random.randint(1, 11) for i in range(n)]
print(my_list)
print(f'элемент {x} в списке встречается {my_list.count(x)} раз')