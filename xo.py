"""Крестики-нолики v1.0"""
import os
import random
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Style.BRIGHT + Fore.GREEN + 'Крестики-Нолики - Cyberpunk Edition.')
print(Style.RESET_ALL)
quit_game = 0


def player_init():  # Инициализация игроков
    global player_1
    while True:
        player_1 = input(
            'Введите имя первого игрока (разрешены буквы и цифры): ')
        if len(player_1) > 20:
            print('Имя слишком большое')
        if not player_1.isalnum():
            print('Введены запрещенные символы')
        else:
            break
    global player_2
    while True:
        player_2 = input(
            'Введите имя второго игрока (разрешены буквы и цифры): ')
        if len(player_2) > 20:
            print('Имя слишком большое')
        if not player_2.isalnum():
            print('Введены запрещенные символы')
        else:
            break
    print('\n')
    global players
    players = [player_1, player_2]
    return players


def clear_cons():  # Очистка консоли
    os.system('cls||clear')
    print(Style.BRIGHT + Fore.GREEN + 'Крестики-Нолики - Cyberpunk Edition')
    if player_1 and player_2:
        print(Fore.YELLOW + f'Играют {player_1} и {player_2}')
    print(Style.RESET_ALL)


def fieldsize_input():  # Инициализация размера поля
    while True:
        global field_size
        field_size = input(
            'Введите размер стороны поля (не больше 9, например, 3): ')
        if field_size.isalpha():
            print('Неверный формат')
        elif ' ' in field_size:
            print('Неверный формат')
        elif int(field_size) > 9:
            print('Неверный формат')
        else:
            print(f'Выбран размер {field_size}x{field_size}\n')
            time.sleep(2)
            break
    global xo_field
    xo_field = [['' for j in range(int(field_size) + 1)]
                for i in range(int(field_size) + 1)]  # создаем поле на 1 больше для показа координат.
    for i in range(len(xo_field)):  # подписываем горизонтальные координаты.
        xo_field[0][i] = str(i)
    for i in range(len(xo_field)):  # подписываем вертикальные координаты.
        xo_field[i][0] = str(i)
    return field_size


def field_show():  # Вывод поля
    for i in range(len(xo_field)):
        for j in range(len(xo_field)):
            if xo_field[i][j] == 'X':
                print(Style.BRIGHT + Fore.RED, end='')
                print('X', end='   ')
                print(Style.RESET_ALL, end='')
            elif xo_field[i][j] == 'O':
                print(Style.BRIGHT + Fore.WHITE, end='')
                print('O', end='   ')
                print(Style.RESET_ALL, end='')
            elif xo_field[i][j] == '':
                print(' ', end='   ')
            else:
                print(Style.DIM, end='')
                print(xo_field[i][j], end='   ')
                print(Style.RESET_ALL, end='')
        print('\n')


player_init()
clear_cons()
fieldsize_input()
clear_cons()


# Партия игры
queue = random.choice(players)
print(Fore.CYAN + 'Очередность определена случайным образом.')
print(Style.RESET_ALL)
time.sleep(2)
clear_cons()

print(Fore.CYAN +
      'Для того, чтобы поставить знак, введите координаты в формате "12"\n(где первая цифра это горизонталь, вторая - вертикаль)')
print(Style.RESET_ALL)

xo_field[1][1] = 'X'
xo_field[1][2] = 'O'
xo_field[1][3] = 'X'
xo_field[2][1] = 'O'
xo_field[2][2] = 'X'
xo_field[2][3] = 'O'
xo_field[3][1] = 'X'
xo_field[3][2] = 'O'
xo_field[3][3] = 'X'

field_show()


player_turn = input(Style.BRIGHT + Fore.GREEN + f'Ходит {queue}: ')
print(Style.RESET_ALL)

# возвращаем в очередь следующего игрока
queue = players[(players.index(queue) + 1) % 2]


queue = players[(players.index(queue) + 1) % 2]
player_turn = input(f'Ходит {queue}: ')
