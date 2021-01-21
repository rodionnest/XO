import time
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

    #  Создаем массив диагоналей поля
    d = 0
    xo_field_diag_arr = []
    while True:
        xo_field_diag = []
        j = (len(xo_field)-1)-d
        k = 0
        if j < 0:
            k = -j
            j = 0
        while j < len(xo_field) and k < len(xo_field[j]):
            xo_field_diag.append(xo_field[j][k])
            j += 1
            k += 1
        if len(xo_field_diag) == 0:
            break
        d += 1
        xo_field_diag_arr.append(xo_field_diag)

    #  Проверяем совпадение у получившегося массива

    for i in range(len(xo_field_diag_arr)):
        for j in range(len(xo_field_diag_arr[i])):
            if not compar_char and (xo_field_diag_arr[i][j] == 'X' or xo_field_diag_arr[i][j] == 'O'):
                compar_char = xo_field_diag_arr[i][j]
                counter += 1
            elif compar_char == xo_field_diag_arr[i][j] and (xo_field_diag_arr[i][j] == 'X' or xo_field_diag_arr[i][j] == 'O'):
                counter += 1
            elif compar_char != xo_field_diag_arr[i][j] and (xo_field_diag_arr[i][j] == 'X' or xo_field_diag_arr[i][j] == 'O'):
                compar_char = xo_field_diag_arr[i][j]
                counter = 1
            if counter == int(charcount_win):
                result = 'win'
                break
    counter = 0

    #  Отзеркаливаем массив
    xo_field_mirror = xo_field.copy()
    for i in range(len(xo_field_mirror)):
        xo_field_mirror[i].reverse()

    #  Создаем массив диагоналей отзеркаленного поля
    d = 0
    xo_field_diag_arr = []
    while True:
        xo_field_diag = []
        j = (len(xo_field_mirror)-1)-d
        k = 0
        if j < 0:
            k = -j
            j = 0
        while j < len(xo_field_mirror) and k < len(xo_field_mirror[j]):
            xo_field_diag.append(xo_field_mirror[j][k])
            j += 1
            k += 1
        if len(xo_field_diag) == 0:
            break
        d += 1
        xo_field_diag_arr.append(xo_field_diag)
    print(xo_field_diag_arr)

    #  Проверяем совпадение у получившегося массива

    for i in range(len(xo_field_diag_arr)):
        for j in range(len(xo_field_diag_arr[i])):
            if not compar_char and (xo_field_diag_arr[i][j] == 'X' or xo_field_diag_arr[i][j] == 'O'):
                compar_char = xo_field_diag_arr[i][j]
                counter += 1
            elif compar_char == xo_field_diag_arr[i][j] and (xo_field_diag_arr[i][j] == 'X' or xo_field_diag_arr[i][j] == 'O'):
                counter += 1
            elif compar_char != xo_field_diag_arr[i][j] and (xo_field_diag_arr[i][j] == 'X' or xo_field_diag_arr[i][j] == 'O'):
                compar_char = xo_field_diag_arr[i][j]
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


xo_field = [
    ['X', '', 'X'],
    ['', 'O', 'O'],
    ['X', 'O', 'X'],
]


check_finish()
