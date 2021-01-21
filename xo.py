"""Крестики-Нолики - Cyberpunk Edition. v1.0."""
import os
import random
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

title = 'Крестики-Нолики - Cyberpunk Edition.v.1.0.'
print(Style.BRIGHT + Fore.GREEN + title)
print(Style.RESET_ALL)

chars = ['X', 'O']
field_size = 0  # fieldsize_input()
xo_field = []

player_1 = None  # player_init()
player_2 = None  # player_init()
players = []  # player_init()

result = None
game_quit = 0
counter = 0
compar_char = None
charcount_win = 3


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


def clear_cons():  # Очистка консоли и вывод игроков
    os.system('cls||clear')
    print(Style.BRIGHT + Fore.GREEN + title)
    if player_1 and player_2:
        print(Fore.YELLOW + f'Играют {player_1} и {player_2}')
    print(Style.RESET_ALL)


def fieldsize_input():  # Инициализация размеров поля
    global field_size
    while True:

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
    global charcount_win
    while True:
        charcount_win = input(
            f'Введите количество знаков подряд для выигрыша (меньше либо равно {field_size} и больше 2): ')
        if not field_size.isdigit():
            print('Неверный формат')
        elif int(charcount_win) < 3:
            print('Количество должно быть больше 2')
        elif int(charcount_win) > int(field_size):
            print('Количество должно быть меньше размера поля')
        else:
            if charcount_win == '3' or charcount_win == '4':
                print(f'Выбрано {charcount_win} знака для выигрыша\n')
                time.sleep(1.5)
            else:
                print(f'Выбрано {charcount_win} знаков для выигрыша\n')
                charcount_win = int(charcount_win)
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
    global xo_field
    global result
    global charcount_win
    global counter
    global compar_char

    #  Проверяем горизонтальное совпадение
    for i in range(len(xo_field)):
        for j in range(len(xo_field[i])):
            if not compar_char and (xo_field[i][j] == 'X' or xo_field[i][j] == 'O'):
                compar_char = xo_field[i][j]
                counter += 1
            elif compar_char == xo_field[i][j] and (xo_field[i][j] == 'X' or xo_field[i][j] == 'O'):
                counter += 1
            elif compar_char != xo_field[i][j] and (xo_field[i][j] == 'X' or xo_field[i][j] == 'O'):
                compar_char = xo_field[i][j]
                counter = 1
            if counter == int(charcount_win):
                result = 'win'
                break
        counter = 0

    #  Разворачиваем поле на 90 градусов
    xo_fieldrotate = []
    for i in range(len(xo_field)):
        xo_fieldrotate.append([])
        for j in range(len(xo_field[i])):
            xo_fieldrotate[i].append(xo_field[j][i])

    #  Проверяем горизонтальное совпадение у получившегося массива
    for i in range(len(xo_fieldrotate)):
        for j in range(len(xo_fieldrotate[i])):
            if not compar_char and (xo_fieldrotate[i][j] == 'X' or xo_fieldrotate[i][j] == 'O'):
                compar_char = xo_fieldrotate[i][j]
                counter += 1
            elif compar_char == xo_fieldrotate[i][j] and (xo_fieldrotate[i][j] == 'X' or xo_fieldrotate[i][j] == 'O'):
                counter += 1
            elif compar_char != xo_fieldrotate[i][j] and (xo_fieldrotate[i][j] == 'X' or xo_fieldrotate[i][j] == 'O'):
                compar_char = xo_fieldrotate[i][j]
                counter = 1
            if counter == int(charcount_win):
                result = 'win'
                break
        counter = 0

    #  Проверка ничьей
    full_field = []
    for i in xo_field:
        full_field.append(all(i))
    if all(full_field) and not result:
        result = 'draw'
    print(result)
    time.sleep(0.2)


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
while not result:
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
    check_finish()
    time.sleep(0.2)
    clear_cons()
    # возвращаем в очередь следующего игрока
    queue = players[(players.index(queue) + 1) % 2]
    chars_queue = (chars_queue + 1) % 2  # возвращаем следующий знак
    field_show()

print(Style.BRIGHT + Fore.RED + f'Победил {queue}!')
print(Style.BRIGHT + Fore.GREEN + 'Всего Вам наилучшего, заходите еще!')
print(Style.RESET_ALL)
