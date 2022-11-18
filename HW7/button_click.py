import export_data as exp
import import_data as imp
import wiew

def button_click():
    wiew.hello()
    choise = wiew.button()
    while choise != 'q':
        if choise == '1':
            exp.export_data()
        elif choise == '2':
            what_find = input('Для поиска по фамилии введите "1"\nДля поиска по имени введите "2"\nДля поиска по номеру телефона введите "3"\n')
            if what_find == '1': imp.find_surname(input('Введите фамилию: '))
            if what_find == '2': imp.find_name(input('Введите имя: '))
            if what_find == '3': imp.find_phone(input('Введите телефон: '))
        choise = wiew.button()