"""Крестики-нолики v1.0"""
print('Добро пожаловать в игру Крестики-Нолики\n')

# Инициализация игроков


def player_init():
    global player_1
    player_1 = input('Введите имя первого игрока: ')
    global player_2
    player_2 = input('Введите имя второго игрока: ')
    return player_1, player_2


# Инициализация размера поля
def fieldsize_input():
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
    xo_field = [['' for j in range(int(field_size) + 1)]  # создаем поле на 1 больше для показа координат.
                for i in range(int(field_size) + 1)]
    return field_size


fieldsize_input()
for i in xo_field:
    print(i)


# Вывод поля
# def field_show():


# Партия игры
