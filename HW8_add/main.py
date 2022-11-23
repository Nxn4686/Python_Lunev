# # Написать функцию num_translate(), переводящую числительные от 0 до 10
# c английского на русский язык.
# number = input('введите число от 0 до 10 на английском: ')
# def translate(number):
#
#     eng_to_rus_translate = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
#                 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять', 'zero': 'ноль','One': 'Oдин', 'Two': 'Два', 'Three': 'Tри', 'Four': 'Четыре', 'Five': 'Пять', 'Six': 'Шесть',
#                 'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Ten': 'Десять', 'Zero': 'Ноль'}
#     if number not in eng_to_rus_translate:
#         print('None')
#     elif number.istitle():
#         print(f'{number.capitalize()} по русски: {eng_to_rus_translate[number].capitalize()}')
#     else:
#         print(f'{number} по русски: {eng_to_rus_translate[number]}')
#
# translate(number)


# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
# возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы.
# Например:thesaurus("Иван", "Мария", "Петр", "Илья")
# {"И": ["Иван", "Илья"], "М": ["Мария"], "П": ["Петр"]}

def thesaurus(*args):
    some_list = list(args)
    some_dict = {}
    for i in range(len(some_list)):
        if some_list[i][0] in some_dict.keys(): #
            some_dict[some_list[i][0]].append(some_list[i])
        else:
            some_dict[some_list[i][0]] = [some_list[i]]
    print(some_dict)

thesaurus("Иван", "Мария", "Петр", "Илья", "Петро", "Федор")

# thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")