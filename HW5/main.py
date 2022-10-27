# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# РЕШЕНИЕ:
# text = input('Введите текст слова через пробел')
# text = text.split()
# new_text = list(filter(lambda i: 'абв' not in i, text))
# print(new_text)
# # ======================================================================
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока
# делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента
# достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# РЕШЕНИЕ:

# from random import randint
#
# name1 = input('Ввведите имя первого игрока: ')
# name2 = input('Ввведите имя второго игрока: ')
# candy = int(input('Ввведите количество конфет на столе: '))
#
# flag = randint(0, 2)
# if flag == 1:
#     print(f'Первый ходит {name1}')
#     player1 = name1
# else:
#     print(f'Первый ходит {name2}')
#     player2 = name2
#
# while candy > 0:
#     if flag:
#         flag = False
#         print(f'{str(name1)}, какое количество конфет возьмете? ')
#         k = int(input())
#         if k > 28:
#             print('Можно взять не больше 28 конфет')
#         else:
#             candy -= k
#             if candy == 0:
#                 print(f'Победил {str(name1)}')
#             else:
#                 print(f'Осталось {candy} конфет ')
#     else:
#         flag = True
#         if candy > 0:
#             print(f'{str(name2)}, какое количество конфет возьмете? ')
#             k = int(input())
#         if k > 28:
#             print('Можно взять не больше 28 конфет')
#         else:
#             candy -= k
#         if candy == 0:
#             print(f'Победил {str(name2)}')
#         else:
#             print(f'Осталось {candy} конфет ')

# ================================================================================
# Создайте программу для игры в ""Крестики-нолики"".

# Используемые функции в программе
# draw_board() – рисует игровое поле в привычном для человека формате.
# take_input() – принимает ввод пользователя. Проверяет корректность ввода.
# check_win – функция проверки игрового поля, проверяет, выиграл ли игрок.
# main() – основная функция игры, которая будет запускать все ранее описанные функции.
# Данная функция запускает и управляет игровым процессом.
# board = list(range(1, 10))
#
# def draw_board(board):
#     print("_" * 13)
#     for i in range(3):
#         print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
#         print("-" * 13)
# draw_board(board)

#
# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")
#
# def check_win(board):
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False
#
# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)



# ===============================================================
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('symb', 'r', encoding='utf-8') as s:
    some_list = s.read()

print(some_list)
s = str(some_list)


def count_symbols(s):
    new_s = ''  # сохраняет выходную строку
    i = 0
    while i < len(s):
        count = 1  # подсчитывает количество вхождений символа в индексе `i`
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        new_s += str(count) + s[i]  # добавляет к результату текущий символ и его количество
        i += 1
    return new_s

print(count_symbols(s))

with open('countSymbols.txt', 'w') as f:
    f.write(count_symbols(s))