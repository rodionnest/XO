"""Крестики-нолики v1.0"""
import os
import random
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

title = 'Крестики-Нолики - Cyberpunk Edition.'
print(Style.BRIGHT + Fore.GREEN + title)
print(Style.RESET_ALL)
chars = ['X', 'O']
game_quit = 0
game_win = 0
game_draw = 0


def player_init():  # Инициализация игроков
    global player_1
    while True:
        player_1 = input(
            'Введите имя первого игрока (разрешены буквы и цифры): ')
        if len(player_1) > 20:
            print('Имя слишком большое')
        elif player_1.count(' ') == len(player_1):
            print('Имя не может содержать только пробелы')
        else:
            break
    global player_2
    while True:
        player_2 = input(
            'Введите имя второго игрока (разрешены буквы и цифры): ')
        if len(player_2) > 20:
            print('Имя слишком большое')
        elif player_2.count(' ') == len(player_2):
            print('Имя не может содержать только пробелы')
        else:
            break
    print('\n')
    global players
    players = [player_1, player_2]
    return players


def clear_cons():  # Очистка консоли
    os.system('cls||clear')
    print(Style.BRIGHT + Fore.GREEN + title)
    if player_1 and player_2:
        print(Fore.YELLOW + f'Играют {player_1} и {player_2}')
    print(Style.RESET_ALL)


def fieldsize_input():  # Инициализация размеров поля
    while True:
        global field_size
        field_size = input(
            'Введите размер стороны поля (от 3 до 9): ')
        if not field_size.isdigit():
            print('Неверный формат')
        elif not (2 < int(field_size) < 10):
            print('Неверный размер')
        else:
            print(f'Выбран размер {field_size}x{field_size}\n')
            time.sleep(1.5)
            break
    global xo_field
    xo_field = [['' for j in range(int(field_size) + 1)]
                for i in range(int(field_size) + 1)]  # создаем поле на 1 больше для показа координат.
    for i in range(len(xo_field)):  # подписываем горизонтальные координаты.
        xo_field[0][i] = str(i)
    for i in range(len(xo_field)):  # подписываем вертикальные координаты.
        xo_field[i][0] = str(i)
    return field_size


def charcountwin_input():  # Количество знаков подряд для выигрыша
    while True:
        global сharcount_win
        сharcount_win = input(
            f'Введите количество знаков подряд для выигрыша (меньше либо равно {field_size} и больше 2): ')
        if not field_size.isdigit():
            print('Неверный формат')
        elif int(сharcount_win) < 3:
            print('Количество должно быть больше 2')
        elif int(сharcount_win) > int(field_size):
            print('Количество должно быть меньше размера поля')
        else:
            if сharcount_win == '3' or сharcount_win == '4':
                print(f'Выбрано {сharcount_win} знака для выигрыша\n')
                time.sleep(1.5)
            else:
                print(f'Выбрано {сharcount_win} знаков для выигрыша\n')
                time.sleep(1.5)
            break


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


def check_finish():  # Проверка условий окончания партии #! ДОРАБАТЫВАЕМ ПРОВЕРКУ УСЛОВИЙ ФИНИША
    full_field = []
    for i in xo_field:
        full_field.append(all(i))
    if all(full_field) and game_win == 0:
        return 0


player_init()
clear_cons()
fieldsize_input()
clear_cons()
charcountwin_input()
clear_cons()

# Партия игры
queue = random.choice(players)
print(Fore.CYAN + 'Очередность определена случайным образом.')
print(Style.RESET_ALL)
time.sleep(1.5)
clear_cons()

field_show()


chars_queue = 0

while True:
    print(Fore.CYAN +
          'Для того, чтобы поставить знак, введите координаты в формате "12"\n(где первая цифра это горизонталь, вторая - вертикаль)')
    print(Style.RESET_ALL)
    while True:
        player_turn = input(Style.BRIGHT + Fore.GREEN +
                            f'Ходит {queue} ({chars[chars_queue]}): ')
        print(Style.RESET_ALL)
        if len(player_turn) != 2 or not player_turn.isdigit():
            print('Неверный формат')
        elif int(player_turn[0]) > int(field_size) or int(player_turn[1]) > int(field_size):
            print('Неверное значение')
        elif xo_field[int(player_turn[1])][int(player_turn[0])] != '':
            print('Знак в этом месте уже есть')
        else:
            break

    xo_field[int(player_turn[1])][int(player_turn[0])] = chars[chars_queue]
    clear_cons()

    # возвращаем в очередь следующего игрока
    queue = players[(players.index(queue) + 1) % 2]
    chars_queue = (chars_queue + 1) % 2  # возвращаем следующий знак
    field_show()
