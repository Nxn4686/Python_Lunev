from datetime import datetime

def log(id):
    time = datetime.now().strftime('%H:%M')
    some_list_1 = ['Внесение данных в ', 'Поиск данных в ']
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write(f'{some_list_1[id]} {time}\n')

