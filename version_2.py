# DONE: board
# DONE: display board
# TODO: handle turns
# TODO: flip player
# TODO: checkWinner
    # TODO: check rows
    # TODO: check columns
    # TODO: check diagonals
# TODO: checkTie
# TODO: display winner

# ----------- Global Variables ----------- #
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
current_player = "X"
is_game_active = True
winner = None

def checkRow():
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
    
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return


def checkColumn():
    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'
    
    if column1:
        return board[0]
    elif column2:
        return board[3]
    elif column3:
        return board[6]
    return


def checkDiagonal():
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[6] == board[4] == board[2] != '-'
    
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[3]
    return


def checkTie():
    global is_game_active

    if "-" not in board:
        is_game_active = False
    return


def checkWinner():
    global is_game_active, winner

    row_winner = checkRow()
    column_winner = checkColumn()
    diagonal_winner = checkDiagonal()

    if row_winner or column_winner or diagonal_winner:
        is_game_active = False

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    return


def flipPlayers():
    # Setup global variables
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


def handleTurns():
    # Setup global variables
    global current_player

    print("\n__" + current_player + "'s Turn__")
    position = input("Choose position (1-9): ")
    
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose position (1-9): ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
            board[position] = current_player
        else:
            print("\nPosition is taken. Try again.\n")

    display_board()
    return


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("__________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("__________")
    print(board[6] + " | " + board[7] + " | " + board[8])


def start_game():
    display_board()
    
    while is_game_active:
        handleTurns()

        flipPlayers()

        checkWinner()

        checkTie()
    
    if winner == "X" or winner == "O":
        print(winner + " won.")
    else: 
        print("Tie.")
    return


start_game()