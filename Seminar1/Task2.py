#Задача 2: Найдите сумму цифр трехзначного числа.
#*Пример:*
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)
number_s = input('Введите трехзначное число: ')
if len(number_s) == 3 and number_s.isdigit():
    number = int(number_s)
    print(f'вы ввели число {number}')
    number1 = number % 10
    variable = number // 10
    number2 = variable % 10
    number3 = variable // 10
    print(f'первое число: {number3}, второе число: {number2}, третье число: {number1}')
    print('Сумма чисел трехзначного числа равна: ', number1 + number2 + number3)
else:
    print('Введите пожалуйста корректные данные (целое положительное трехзначное число!)')
