import os.path
import csv
import import_data
import log

id_process = 0
def export_data():

    id = import_data.find_id()
    if not os.path.exists('data.csv'):
        with open('data.csv', 'w', encoding='utf-8') as dt:
            writer = csv.writer(dt, delimiter=';')
            writer.writerow(('id','number school','surname', 'name', 'Number of class', 'info'))
    exit = ''

    while exit != 'q':
        log.log(id_process)
        users_data = [
            [id+1, input('введите номер школы: '),input('введите фамилию: '), input('введите имя: '), input('Введите класс: '),
             input('пару слов о себе: ')]
        ]
        id += 1
        with open('data.csv', 'a', encoding='utf-8') as dt:
            writer = csv.writer(dt, delimiter=';')
            writer.writerows(
                users_data
            )

        exit = input('Для завершения ввода данных нажмите "q"\nДля продолжения нажмите "Enter"\n')




