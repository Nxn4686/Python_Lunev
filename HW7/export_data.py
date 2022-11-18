import os.path
import csv

def export_data():
    if not os.path.exists('data.csv'):
        with open('data.csv', 'w', encoding='utf-8') as dt:
            writer = csv.writer(dt, delimiter=';')
            writer.writerow(('surname', 'name', 'Phone', 'info'))
    exit = ''
    while exit != 'q':
        users_data = [
            [input('введите фамилию: '), input('введите имя: '), input('введите номер телефона: '),
             input('пару слов о себе: ')]
        ]

        with open('data.csv', 'a', encoding='utf-8') as dt:
            writer = csv.writer(dt, delimiter=';')
            writer.writerows(
                users_data
            )

        exit = input('Для завершения ввода данных нажмите "q"\nДля продолжения нажмите "Enter"\n')
