

# ------------------------------------------HW---------------------------------------------
# Реализуйте классы MinStat, MaxStat, AverageStat, которые будут находить минимум,
# максимум и среднее арифметическое последовательности целых чисел.
# Экземпляры классов инициализируются без аргументов. Метод add_number должен добавлять
# в статистику число, которое будет учтено при вычислении финального результата методом result.
# Для экземпляров MinStat и MaxStat result должен возвращать целое число,
# для AverageStat — число типа float (это число будет сравниваться с правильным ответом
# до седьмой значащей цифры).
# Если в последовательности отсутствуют числа и статистические величины вычислить невозможно,
# метод result должен возвращать None.

# -----------------------------------TASK 1--------------------------------------------------

# class MinStat:
#
#     def __init__(self):
#         self.number = []
#
#     def add_number(self, n):
#         self.number.append(n)
#
#     def result(self):
#         if self.number == []:
#             return None
#         else:
#             return min(self.number)
#
#
# class MaxStat:
#
#     def __init__(self):
#         self.number = []
#
#     def add_number(self,n):
#         self.number.append(n)
#
#     def result(self):
#         if self.number == []:
#             return None
#         else:
#             return max(self.number)
#
# class AverageStat:
#
#     def __init__(self):
#         self.number=[]
#
#     def add_number(self,n):
#         self.number.append(n)
#
#     def result(self):
#         if self.number == []:
#             return None
#         else:
#             return sum(self.number)/len(self.number) #сумма и количество элементов
#
# Проверка
# print("Пример 1.")
# values = [1, 2, 4, 5]
#
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)
#
# print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))
#
# print('Пример 2.')
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
#
# print(mins.result(), maxs.result(), average.result())
#
# print('Пример 3.')
# values = [1, 0, 0]
#
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)
#
# print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))


# ---------------------------------TASK 2---------------------------------------
# Реализуйте класс Table, который хранит целые числа в двумерной таблице.
# При инициализации Table(rows, cols) экземпляру передаются число строк и столбцов в таблице.
# Строки и столбцы нумеруются с нуля.
# table.get_value(row, col) — прочитать значение из ячейки в строке row, столбце col.
# Если ячейка с индексами row и col не лежит внутри таблицы, нужно вернуть None.
# table.set_value(row, col, value) — записать число в ячейку строки row, столбца col.
# Гарантируется, что в тестах будет в запись только в ячейки внутри таблицы.
# table.n_rows() — вернуть число строк в таблице
# table.n_cols() — вернуть число столбцов в таблице
# table.delete_row(row) — удалить строку с номером row
# table.delete_col(col) — удалить колонку с номером col
# table.add_row(row) — добавить в таблицу новую строку с индексом row.
# Номера строк >= row, должны увеличиться на единицу. Новая строка состоит из нулей.
# table.add_col(col) — добавить в таблицу новую колонку с индексом col.
# Номера колонок >= col, должны увеличиться на единицу. Новая колонка состоит из нулей.

class Table(object):

    def __init__(self, rows, cols):
        self.rows = rows  # строка
        self.cols = cols  # столбец
        # self.table = [[0] * cols] * rows # почему так нельзя???
        self.table = [[0] * cols for i in range(rows)]

    def get_value(self, row, col):
        if self.rows > row >= 0 and self.cols > col >= 0:
            return self.table[row][col]
        else:
            return None

    def set_value(self, row, col, value):
        self.table[row][col] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols

    def delete_row(self, row):
        del self.table[row]
        self.rows -= 1

    def delete_col(self, col):
        for row in range(self.rows): # для каждой строки в диапозоне (self.rows)
            self.table[row].pop(col) # удалить столбец с элементом 0 в строку [row]
        self.cols -= 1

    def add_row(self, row):
        self.table.insert(row, [0] * self.cols)
        self.rows += 1

    def add_col(self, col):
        for row in range(self.rows):  # для каждой строки в диапозоне (self.rows)
            self.table[row].insert(col, 0)  # добавить столбец с элементом 0 в строку [row]
        self.cols += 1


print("Пример 1.")
tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
#
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

print("Пример 2.")
tab = Table(2, 2)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.set_value(0, 0, 10)
tab.set_value(0, 1, 20)
tab.set_value(1, 0, 30)
tab.set_value(1, 1, 40)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(0)
tab.add_col(1)

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

print("Пример 3.")
tab = Table(1, 1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.set_value(0, 0, 1000)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(0)
tab.add_row(2)
tab.add_col(0)
tab.add_col(2)

tab.set_value(0, 0, 2000)
tab.set_value(0, 2, 3000)
tab.set_value(2, 0, 4000)
tab.set_value(2, 2, 5000)

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()