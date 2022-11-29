# # --------------------ДЗ Крестики нолики------------------------------------------
# # Напишите класс TicTacToeBoard для игры в крестики-нолики, который должен иметь следующие методы:
# # new_game() – для создания новой игры;
# # get_field() – для получения поля (список списков);
# # check_field() – для проверки, есть ли победитель, который возвращает X,
# # если победил первый игрок, 0, если второй, D, если ничья и None, если можно продолжать игру;
#
# # make_move(row, col) – который устанавливает значение текущего хода в ячейку поля с координатами row, col,
# # если это возможно, «переключает» ход игрока, а также возвращает сообщение «Победил игрок X» при победе крестиков,
# # «Победил игрок 0» при победе ноликов, «Ничья» в случае ничьей и «Продолжаем играть», если победитель после
# # данного хода неопределён.
# # Кроме того, метод make_move должен возвращать сообщение «Клетка <row>, <col> уже занята», если в клетке уже
# # стоит крестик или нолик, и «Игра уже завершена», если в текущей игре уже выявлен победитель или закончились
# # ячейки для ходов.
# # При создании объекта класса должна создаваться новая игра.
# # Аргументы row и col метода make_move могут принимать значения от 1 до 3.
#
# class TicTacToeBoard:
#
#     def __init__(self):
#         self.field = []
#         for row in range(3):
#             r = []
#             for col in range(3):
#                 r.append('-')
#             self.field.append(r)
#         self.move_x = True
#         self.end_of_game = False
#         self.winner = None
#         self.win = ''
#         self.first_move = True
#
#     def new_game(self):
#         self.field = []
#         for row in range(3):
#             r = []
#             for col in range(3):
#                 r.append('-')
#             self.field.append(r)
#             self.move_x = True
#             self.end_of_game = False
#             self.winner = None
#             self.win = ''
#             self.first_move = True
#
#     def get_field(self):
#         return self.field
#
#     def check_field(self):
#         if self.win == 'X':
#             return 'X'
#         elif self.win == 'O':
#             return 'O'
#         elif self.win == 'ничья':
#             return 'D'
#         else:
#             return None
#
#     def make_move(self, row, col):
#         if self.end_of_game and not self.first_move:
#             return 'Игра уже завершена'
#         else:
#             if self.field[row - 1][col - 1] != '-':
#                 return f'Клетка {row}, {col} уже занята'
#             else:
#                 if self.move_x:
#                     self.field[row - 1][col - 1] = 'X'
#                     self.move_x = False
#                     self.first_move = False
#                 else:
#                     self.field[row - 1][col - 1] = 'O'
#                     self.move_x = True
#                     self.first_move = False
#             if self.field[0].count(self.field[0][0]) == 3 and self.field[0][0] != '-':
#                 self.end_of_game = True
#                 self.win = self.field[0][0]
#                 return f'Победил игрок {self.field[0][0]}'
#             elif self.field[1].count(self.field[1][0]) == 3 and self.field[1][0] != '-':
#                 self.end_of_game = True
#                 self.win = self.field[1][0]
#                 return f'Победил игрок {self.field[1][0]}'
#             elif self.field[2].count(self.field[2][0]) == 3 and self.field[2][0] != '-':
#                 self.end_of_game = True
#                 self.win = self.field[2][0]
#                 return f'Победил игрок {self.field[2][0]}'
#             elif self.field[0][0] == self.field[1][0] == self.field[2][0] and self.field[0][0] != '-':
#                 self.end_of_game = True
#                 self.win = self.field[0][0]
#                 return f'Победил игрок {self.field[0][0]}'
#             elif self.field[0][1] == self.field[1][1] == self.field[2][1] and self.field[0][1] != '-':
#                 self.end_of_game = True
#                 self.win = self.field[0][1]