field = [[" "] * 3 for i in range(3)]

#field[0][1] = "X"

def show_map(): #отображаем поле после каждого хода
    print("  | 0 | 1 | 2 |")
    print("---------------")
    for i in range(3):
        line = " | ".join(field[i])
        print(f"{i} | {line} |")
        print("---------------")

def next_action(sim): #запрашиваем у игрока
    while True:
        coords = input(f"Введите через пробел координаты для {sim} (строка, столбец): ").split()

        if len(coords) != 2:
            print("Нужно ввести 2 координаты")
            continue

        x, y = coords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Нужно ввести цифры от 0 до 2 в качестве координат")
            continue

        x, y = int(x), int(y)
        if x < 0 or y < 0 or x > 2 or y > 2:
            print("Введены некорректные координаты, повторите ввод")
            continue

        if field[x][y] != " ":
            print("Поле занято, введите другие координаты")
            continue

        return x,y


def check_win(): #проверяем победу
    for i in range(3):
        chk_sim = []
        for j in range(3):
            chk_sim.append(field[i][j])

        if chk_sim == ["X","X","X"] or chk_sim == ["0","0","0"]:
             return True

    for i in range(3):
        chk_sim = []
        for j in range(3):
            chk_sim.append(field[j][i])
        if chk_sim == ["X","X","X"] or chk_sim == ["0","0","0"]:
            return True

    chk_sim = []
    for i in range(3):
        chk_sim.append(field[i][i])
    if chk_sim == ["X", "X", "X"] or chk_sim == ["0", "0", "0"]:
        return True

    chk_sim = []
    for i in range(3):
        chk_sim.append(field[i][2-i])
    if chk_sim == ["X", "X", "X"] or chk_sim == ["0", "0", "0"]:
        return True

    return False


simbol = "X"
for i in range(9):
    show_map()
    x, y = next_action(simbol)

    field[x][y] = simbol

    if check_win():
        print(f"Игра окончена. Выиграл игрок {simbol}")
        show_map()
        break

    if simbol == "0":
        simbol = "X"
    else:
        simbol = "0"

    if i == 8:
        print("Ничья!")


