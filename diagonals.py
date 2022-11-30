score = [0, 0]

currentPlayer: int = 1


def new_board(n):
    board = []
    for i in range(n):
        tempBoard = []
        for j in range(n):
            tempBoard.append(0)
        board.append(tempBoard)
    return board


def get_char_by_number(number: int):
    if number == 0:
        return "."
    elif number == 1:
        return "x"
    else:
        return "o"


def display_score():
    print("Current score :", score[0], "vs", score[1])


def display_board(board):
    for x in range(len(board)):
        print(x + 1, "| ", end="")
        for z in range(len(board[x])):
            print(get_char_by_number(board[x][z]), end=" ")
        print()
    print("  -", end="")
    for i in range(len(board) * 2):
        print("-", end="")
    print()
    print("    ", end="")
    for i in range(len(board)):
        print(i + 1, end=" ")
    print()
    display_score()


# Ici je défini la fonction possible_square qui permet de calculer si
# la case que le joueur choisi n'est pas occupé.
def possible_square(board, x: int, z: int):
    if (x >= len(board) or x < 0) and (z >= len(board) or z < 0):
        return False
    return board[x][z] == 0


def select_square(board):
    print("Pour Choisir merci de respecter le format suivant :")
    print("x,z | exemple : 1,5")
    location = input("Choisi les cases : ").split(",")
    if len(location) != 2:
        print("Impossible : respecter le format ! (x,z)")
        location = input("Choisi les cases : ").split(",")

    x = int(location[0]) - 1
    z = int(location[1]) - 1
    while not possible_square(board, x, z):
        print("Impossible veuillez rechoisir une case !")
        location = input("Choisi les cases : ").split(",")
        if len(location) != 2:
            print("Impossible : respecter le format ! (x,z)")
            location = input("Choisi les cases : ").split(",")
        x = int(location[0]) - 1
        z = int(location[1]) - 1
    return location


def update_board(board, player: int, x: int, z: int):
    board[x][z] = player


def again(board):
    for x in range(len(board)):
        for z in range(len(board[x])):
            if board[x][z] == 0:
                return True


def win():
    score1 = score[0]
    score2 = score[1]

    if score1 > score2:
        return "Bravo au joueur 1 qui vient de gagner la partie avec " + str(score1) + " points"
    elif score1 < score2:
        return "Bravo au joueur 2 qui vient de gagner la partie avec " + str(score2) + " points"
    else:
        return "Bravo au 2 joueurs qui ont participer, malheursement il y a execo"


def update_score(board, player: int, x: int, y: int):
    points = 0

    length = len(board)

    if (x == 0 and y == length - 1) or (x == length - 1 and y == 0):

        for i in range(length):
            case = board[i][-(i + 1)]
            if case == player:
                points += 1
            elif case == 0:
                return 0

    if (x == 0 and y == 0) or (x == length - 1 and y == length - 1):
        for i in range(length):
            case = board[i][i]
            if case == player:
                points += 1
            elif case == 0:
                return 0

    else:

        temp_x, temp_z = x, y

        total = [0, 0]

        while x > 0 and y < length - 1:
            x -= 1
            y += 1

        while x <= length - 1 and y >= 0:
            case = board[x][y]
            x += 1
            y -= 1
            if case == player:
                total[0] += 1
            elif case == 0:
                total[0] = 0
                break

        x, y = temp_x, temp_z

        while x > 0 and y > 0:
            x -= 1
            y -= 1

        while x <= length - 1 and y <= length - 1:
            case = board[x][y]
            x += 1
            y += 1
            if case == player:
                total[1] += 1
            elif case == 0:
                total[1] = 0
                break

        points = total[0] + total[1]
    return points


def diagonals():
    board = new_board(1)

    display_board(board)
    currentPlayer = 1

    while again(board):
        location = select_square(board)
        i = int(location[0]) - 1
        j = int(location[1]) - 1
        update_board(board, currentPlayer, i, j)
        score[currentPlayer - 1] += update_score(board, currentPlayer, i, j)

        display_board(board)

        if currentPlayer == 1:
            currentPlayer = 2
        else:
            currentPlayer = 1

    print(win())


diagonals()
