"""Крестики-нолики v1.0"""
import random
import time
print('Добро пожаловать в игру Крестики-Нолики\n')
# ! Убрать пробелы из инициализации чисел. Посмотреть строковые функции, убирающие пробелы с начала и с конца строк


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


def fieldsize_input():  # Инициализация размера поля
    while True:
        global field_size
        field_size = input(
            'Введите размер стороны поля (не больше 10, например, 3): ')
        if field_size.isalpha():
            print('Неверный формат')
        elif int(field_size) > 10:
            print('Неверный формат')
        else:
            print(f'Выбран размер {field_size}x{field_size}\n')
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
            print(xo_field[i][j], end='    ')
        print('\n')


player_init()
fieldsize_input()
time.sleep(3)

# Партия игры
queue = random.choice(players)
print(f'Очередность определена случайным образом. Ходит {queue}\n')
time.sleep(2)
field_show()
print('Введите коорди')


# возвращаем в очередь следующего игрока
queue = players[(players.index(queue) + 1) % 2]
