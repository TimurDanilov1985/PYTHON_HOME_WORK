#Задача №49.
#Создать телефонный справочник с
#возможностью импорта и экспорта данных в
#формате .txt. Фамилия, имя, отчество, номер
#телефона - данные, которые должны находиться
#в файле.
#1. Программа должна выводить данные
#2. Программа должна сохранять данные в
#текстовом файле
#3. Пользователь может ввести одну из
#характеристик для поиска определенной
#записи(Например имя или фамилию
#человека)
#4. Использование функций. Ваша программа
#не должна быть линейной
#Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
#Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
#для изменения и удаления данных.
def saving_data():
    f = open('telephone_directory.txt', 'a', encoding = 'utf - 8')
    surname = input('Введите фамилию:\t')
    name = input('Введите имя:\t')
    patron = input('Введите отчество:\t')
    phone = input('Введите номер телефона:\t')
    list_s = [surname, name, patron, phone]
    f.write(" ".join(list_s))
    f.write('\n')
    f.close() 
    menu()


def output_file():
    print()
    print('Данные файла:')
    print()
    f = open('telephone_directory.txt', 'r', encoding = 'utf - 8')
    print(f.read())
    f.close()
    menu()


def clear():
    f = open('telephone_directory.txt', 'w')
    f.close()
    menu()


def search():
    x = input('Введите характеристику для поиска записи (например имя или фамилию):\t')
    list_found = list()
    temp = 0
    f = open('telephone_directory.txt', 'r', encoding = 'utf - 8')
    lstf = f.readlines()
    print()
    print('Результат по данному запросу:')
    print()
    for i in lstf:
        if x in i:
            print(i)
            temp = 1
    if temp == 0:
        print()
        print('По данному запросу данных не найдено')
    f.close()
    menu()


def change():
    y = input('Введите параметр записи для поиска (имя, фамилия, номер телефона): ')
    f = open('telephone_directory.txt', 'r', encoding = 'utf - 8')
    list_found = list()
    lstf = f.readlines()
    f.close()
    for i in range(len(lstf)):
        if y in lstf[i]:
            list_found.append(lstf[i])
    n = len(list_found)
    if n == 0:
        print()
        print('По этому запросу нет данных для редактирования')
        print()
        menu()
    elif n == 1:
        print()
        print('Найдены данные:')
        print(*list_found)
        old_str = list_found[0]
        new_list = list(old_str.split())
        print('Для изменения фамилии введите "1"')
        print('Для изменения имени введите "2"')
        print('Для изменения отчества введите "3"')
        print('Для изменения номера телефона введите "4"')
        number = input('Введите номер команды: ')
        if number == '1':
            new_list[0] = input('Введите новую фамилию: ') 
        elif number == '2':
            new_list[1] = input('Введите новое имя: ') 
        elif number == '3':
            new_list[2] = input('Введите новое отчество: ') 
        elif number == '4':
            new_list[3] = input('Введите новый номер телефона: ') 
        new_str = " ".join(new_list)
        print(new_str)
        for i in range(len(lstf)):
            if lstf[i] == old_str:
                lstf[i] = new_str + '\n'
    elif n > 1:
        print()
        print('Найдено несколько записей по запросу: ')
        print()
        d = {}
        for i in range(n):
            d[i] = list_found[i]
            print(str(i + 1) + ' ' + list_found[i])
        num = int(input('Введите порядковый номер записи для редактирования: '))
        old_str = d[num - 1]
        new_list = list(old_str.split())
        print('Для изменения фамилии введите "1"')
        print('Для изменения имени введите "2"')
        print('Для изменения отчества введите "3"')
        print('Для изменения номера телефона введите "4"')
        number = input('Введите номер команды: ')
        if number == '1':
            new_list[0] = input('Введите новую фамилию: ') 
        elif number == '2':
            new_list[1] = input('Введите новое имя: ') 
        elif number == '3':
            new_list[2] = input('Введите новое отчество: ') 
        elif number == '4':
            new_list[3] = input('Введите новый номер телефона: ') 
        new_str = " ".join(new_list)
        print(new_str)
        for i in range(len(lstf)):
            if lstf[i] == old_str:
                lstf[i] = new_str + '\n'
    f = open('telephone_directory.txt', 'w', encoding = 'utf - 8')
    f.close()
    f = open('telephone_directory.txt', 'a', encoding = 'utf - 8')
    for i in lstf:
        f.write(i)
    f.close()
    menu()


def delete():
    y = input('Введите параметр записи для удаления (имя, фамилия, номер телефона): ')
    f = open('telephone_directory.txt', 'r', encoding = 'utf - 8')
    list_found = list()
    lstf = f.readlines()
    f.close()
    for i in range(len(lstf)):
        if y in lstf[i]:
            list_found.append(lstf[i])
    n = len(list_found)
    if n == 0:
        print()
        print('По этому запросу нет данных для редактирования')
        print()
        menu()
    elif n == 1:
        print()
        print('Найдены данные:')
        print(*list_found)
        d_str = list_found[0]
        print('Для подтверждения удаления найденной записи введите "y"')
        print('Для отмены удаления введите другой символ')
        dl = input('Введите подтверждение или отмену: ')
        if dl == 'y':
            f = open ('telephone_directory.txt', 'w', encoding = 'utf - 8')
            f.close()
            f = open ('telephone_directory.txt', 'a', encoding = 'utf - 8')
            for i in lstf:
                if i != d_str:
                    f.write(i)
            f.close()
        print(f'Запись {d_str} удалена')
        menu()
    elif n > 0:
        print()
        print('Найдено несколько записей по запросу: ')
        print()
        d = {}
        for i in range(n):
            d[i] = list_found[i]
            print(str(i + 1) + ' ' + list_found[i])
        num = int(input('Введите порядковый номер записи для удаления: '))
        print('Для подтверждения удаления найденной записи введите "y"')
        print('Для отмены удаления введите другой символ')
        dl = input('Введите подтверждение или отмену: ')
        if dl == 'y':
            f = open ('telephone_directory.txt', 'w', encoding = 'utf - 8')
            f.close()
            f = open ('telephone_directory.txt', 'a', encoding = 'utf - 8')
            for i in lstf:
                if i != d[num - 1]:
                    f.write(i)
            f.close()
        print(f'Запись {d[num - 1]} удалена')
        menu()


def menu():
    print('Для занесения данных в файл введите "1"')
    print('Для вывода информации в файле на экран введите "2"')
    print('Для поиска определенной записи введите "3"')
    print('Для изменения и удаления данных в записи введите "4"')
    print('Для выхода из программы введите "q"')
    print('Для удаления записи из файла введите "del"')
    print('Для очистки файла введите "clear!"')
    number = input('Введите число соответствующее команде:\t')
    if number == '1':
        saving_data()
    elif number == '2':
        output_file()
    elif number == 'clear!':
        clear()
    elif number == '3':
        search()
    elif number == 'q':
        exit()
    elif number == '4':
        change()
    elif number == 'del':
        delete()


if __name__ == '__main__':
    menu()