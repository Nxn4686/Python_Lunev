# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# РЕШЕНИЕ:
# number = float(input('Введите число: '))
# accur = input('Введите точность округления: ')
#
#
# def get_accuracy(accur):
#     str_accur = str(accur)
#     if '.' not in str_accur:
#         return 0
#     # Получение строки после точки и возвращение ее длины
#     return len(str_accur[str_accur.index('.') + 1:])
#
#
# print('Ваше число:')
# print(round(number, get_accuracy(accur)))


# ===========================================# ===========================================
# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# РЕШЕНИЕ:

# n = int(input('Введите число: '))
# number_list = []
# #
# def simple_num(n):  # поиск простых чисел
#     lst = []
#     for i in range(2, n + 1):
#         for j in range(2, i):
#             if i % j == 0:
#                 # если делитель найден, число не простое.
#                 break
#         else:
#             lst.append(i)
#     return lst
#
# for g in simple_num(n):
#     if n % g == 0:
#         number_list.append(g)
# print(number_list)
#
# ===========================================# ===========================================

# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# РЕШЕНИЕ:
# Вариант №1
# a = input('Введите числа: ')
# b = set(a)
# print(b)

# Вариант №2 универсальный
# a = input('Введите любые значния: ')
# new_a = []
# for i in a:
#     if i not in new_a:
#         new_a.append(i)
# print(new_a)

# Вариант №3 универсальный ВЕРНЫЙ
# a = input('Введите любые значния: ')
# new_a = []
# for i in a:
#     count = 0
#     for j in a:
#         if i == j:
#             count += 1
#         if count == 2:
#             break
#     if count == 1:
#         print(i)
# ===========================================# ===========================================

# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# РЕШЕНИЕ:

# import random
#
# k = int(input('Введите натуральную степень k: '))
# while k <= 0:
#     k = int(input('Введены не корректные данные! Введите натуральную степень k: '))
#
# result = [0 for i in range(k)]
# koef = random.sample(range(0, 101), k + 1)
# print(f'Рандомные коэффициенты: {koef}')
# for i in range(len(result)):
#     result[i] = f'{koef[i]}x^{k}'
#     k -= 1
# result.append(str(koef[-1]))
# print(f'До обработки: {result}')
# for elem in result:
#     if elem == 0:
#         result.remove(elem)
#     try:
#         ind_x = elem.find('x')
#         d = int(elem[:ind_x])
#     except AttributeError:
#         continue
#     if d == 0 or elem == '0':
#         result.remove(elem)
#     if '^1' in elem:
#         result.remove(elem)
#         result.insert(-1, elem[:elem.find('^1')])
# print(f'После обработки: {result}')
# polynom = ''
# for i in range(len(result) - 1):
#     polynom += f'{result[i]} + '
# polynom += f'{result[-1]} = 0'
# print(polynom)
#
# with open('text.txt', 'w') as f:
#     f.write(polynom)

# ======================= # ========================================

# import random
# some_dict = {0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'}
# k = int(input('Введите натуральную степень k: '))
# coef = [random.randint(0, 100) for _ in range(k + 1)]
# print(coef)
# with open('coef.txt', 'w', encoding='utf-8') as m: #запись результата в техтовый файл
#     for i in range(len(coef)):
#         if k - i != 1 and k - i != 0:
#             m.write(f'{coef[i]}x{some_dict[k - i]} + ')
#         elif k - i == 1:
#             m.write(f'{coef[i]}x + ')
#         elif k - i == 0:
#             m.write(f'{coef[i]} = 0')

# запись еще одного файла для следующей задачи

# k = int(input('Введите натуральную степень k: '))
# coef = [random.randint(0, 100) for _ in range(k + 1)]
# with open('coef2.txt', 'w', encoding='utf-8') as m: #запись результата в техтовый файл
#     for i in range(len(coef)):
#         if k - i != 1 and k - i != 0:
#             m.write(f'{coef[i]}x{some_dict[k - i]} + ')
#         elif k - i == 1:
#             m.write(f'{coef[i]}x + ')
#         elif k - i == 0:
#             m.write(f'{coef[i]} = 0')

# ===========================================# ===========================================

# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# РЕШЕНИЕ:
import re
# Получение данных из файла
# file1 = 'coef.txt'
# file2 = 'coef2.txt'
#
#
# def read_polynom(file):
#     with open(str(file), "r") as data:
#         polynom = data.read()
#         return polynom


# Получение списка кортежей каждого (<коэффициент>, <степень>)
# def convert_polynom(polynom):
#     polynom = polynom.replace('=0', '')  # отсекаем =0
#     polynom = re.sub("[*|^| ]", " ", polynom).split('+')
#     polynom = [char.split(' ') for char in polynom]
#     polynom = [[x for x in list if x] for list in polynom]
#     for i in polynom:
#         if i[0] == 'x': i.insert(0, 1)
#         if i[-1] == 'x': i.append(1)
#         if len(i) == 1: i.append(0)
#     polynom = [tuple(int(x) for x in j if x != 'x') for j in polynom]
#     return polynom


# Получение списка кортежей суммы (<коэф1 + коэф2>, <степень>)
# def fold_polynoms(polynom1, polynom2):
#     x = [0] * (max(polynom1[0][1], polynom2[0][1] + 1))
#     for i in polynom1 + polynom2:
#         x[i[1]] += i[0]
#     res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
#     res.sort(key=lambda r: r[1], reverse=True)
#     return res


# polynom1 = read_polynom(file1)
# polynom2= read_polynom(file2)
#
# pol_1 = convert_polynom(polynom1)
# pol_2 = convert_polynom(polynom2)
#
# print(fold_polynoms(polynom1,polynom2))
