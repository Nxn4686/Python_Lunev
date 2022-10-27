from random import randint

name1 = input('Ввведите имя первого игрока: ')
name2 = 'BOT'
candy = int(input('Ввведите количество конфет на столе: '))

flag = randint(0, 2)
if flag == 1:
    print(f'Первый ходит {name1}')
    player1 = name1
else:
    print(f'Первый ходит BOT')


# ===============================================
# Функция хода бота:
def bot_move(candy):
    count = 0
    if candy % 28 == 0 and candy > 56:
        k = 27
    elif candy <= 56 and candy > 28:
        k = candy - 29
    elif candy <= 28:
        k = candy
    else:
        while candy % 28 != 0:
            candy -= 1
            count += 1

        k = count
    return k


# ===============================================


while candy > 0:
    if flag:
        flag = False
        print(f'{str(name1)}, какое количество конфет возьмете? ')
        k = int(input())
        if k > 28:
            print('Можно взять не больше 28 конфет')
        else:
            candy -= k
            if candy == 0:
                print(f'Победил {str(name1)}')
            else:
                print(f'Осталось {candy} конфет ')
    else:
        flag = True
        if candy > 0:
            k = bot_move(candy)
            candy -= k
            print(f'BOT взял {k} конфет, осталось {candy} конфет ')
        if candy == 0:
            print(f'Победил BOT')
        else:
            print(f'Осталось {candy} конфет ')
