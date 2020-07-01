# ---------- Global Variables ---------- #
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"
is_game_active = True
winner = None

# Display board
def displayBoard():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("_________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("_________")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def handleTurn(current_player):
    print(current_player + "'s Turn.")
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
            print("Position is taken. Try again.")

    displayBoard()
    return

def flipPlayer():
    # Setup global variables
    global current_player
    
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

    return

def check_rows():
    # Setup global variables
    global winner, is_game_active

    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    if row1 or row2 or row3:
        is_game_active = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def check_columns():
    # Setup global variables
    global is_game_active

    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'

    if column1 or column2 or column3:
        is_game_active = False

    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return

def check_diagonals():
    # Setup global variables
    global winner, is_game_active

    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'

    if diagonal1 or diagonal2:
        is_game_active = False

    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    return

def chooseWinner():
    # Setup global variable
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def checkIfTie():
    # Setup global variable
    global is_game_active

    if "-" not in board:
        is_game_active = False
    
    return

# Start game
def startGame():
    # Setup global variables
    global current_player

    # Initialize board
    displayBoard()

    while is_game_active:
        # handle if it's X or O turn
        handleTurn(current_player)

        flipPlayer()

        # check who wins
        chooseWinner()

        # check if it's a tie
        checkIfTie()

    if(winner!=None):
        print(winner + "'s won.")
    else:
        print("Tie.")
    return

startGame()