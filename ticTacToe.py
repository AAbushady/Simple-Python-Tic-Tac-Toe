"""
This is a simple Tic Tac Toe program based off of the tutorial by Clever Programmer.

The goal of this program is to create a Tic Tac Toe game using an array and mutliple
variables and functions. It will also make use of global variables.
"""

# Board Array to create the Game Board.
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

# ---- Global Variables ----- #

# Variable for continuing the game.
in_progress = True

# Check for a winner.
winner = None

# Set player 1 as "X"
current_player = "X"

# ---- End of Global Variables ----#

# Printing the Game Board into the console.
def display_board():
    # Create Row 1
    print(board[0] + " | " + board[1] + " | " + board[2])
    # Create Row 2
    print(board[3] + " | " + board[4] + " | " + board[5])
    # Create Row 3
    print(board[6] + " | " + board[7] + " | " + board[8])

# Handle a single player's turn.
def handle_turn(player):
    # Display the which player's turn it is.
    print(player + "'s turn.")
    # Take user input for processing.
    position = input("Choose a position from 1 - 9: ")
    
    # valid is created as False in order to check for valid input.
    valid = False
    
    # This while loop will make sure input is valid before adding it to the game board.
    while not valid:
        # While the user input is not one of the valid choices. The user will be
        # prompted until valid input is entered.
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1 - 9: ")
            
        # Convert user input into an integer that can corrrespond to the
        # index of the array.
        position = int(position) - 1

        # If statement for making sure that the space chosen by the user
        # is a valid space. If space is occupied by "X" or "O" user will
        # recieve a message indicating it is an invalid entry.
        if board[position] == "-":
            valid = True
        else:
            print("Occupied! Pick a new Space.")
      
    # Place "X" or "O" based on which user has entered input.
    board[position] = player

    # Show updated Game Board.
    display_board()

def check_rows():
  #Call global variable
    global in_progress

 # Check rows for "X" or "O"
    row_1 = board[0] == board[1] == board[2] !="-"
    row_2 = board[3] == board[4] == board[5] !="-"
    row_3 = board[6] == board[7] == board[8] !="-"

  # Catches if there is a win by row and ends game.
    if row_1 or row_2 or row_3:
        in_progress = False
  
  # Chooses the winning player's symbol to return who won the game.
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return   


def check_columns():
    #Call global variable
    global in_progress

    # Check columns for "X" or "O"
    column_1 = board[0] == board[3] == board[6] !="-"
    column_2 = board[1] == board[4] == board[7] !="-"
    column_3 = board[2] == board[5] == board[8] !="-"

    # Catches if there is a win by column and ends game.
    if column_1 or column_2 or column_3:
        in_progress = False
  
    # Chooses the winning player's symbol to return who won the game.
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return   

def check_diagonals():
    #Call global variable
    global in_progress

    # Check diagonals for "X" or "O"
    diagonal_1 = board[0] == board[4] == board[8] !="-"
    diagonal_2 = board[6] == board[4] == board[2] !="-"

    # Catches if there is a win by column and ends game.
    if diagonal_1 or diagonal_2:
        in_progress = False
  
    # Chooses the winning player's symbol to return who won the game.
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return   

def check_winner():
    # Call global variable
    global winner

    # Call check_rows to see if there is a winner by Row.
    row_winner = check_rows()
    
    # Call check_columns to see if there is a winner by Columns.
    column_winner = check_columns()
    
    #  Call check_diagonals to see if there is a winner by Diagonal.
    diagonal_winner = check_diagonals()
    
    # Assign winner based off of which version of win has been achieved.
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        # If no winner has been found. A tie will be declared by keeping
        # winner as None.
        winner = None
    return

def check_tie():
    # Call in Global variable.
    global in_progress

    # This if statement will end the game if there are no
    # empty spaces left declaring a tie.
    if "-" not in board:
        in_progress = False
    return

def flip_player():
    # Call Global Variable.
    global current_player
    # If the current player was X, make it O
    if current_player == "X":
        current_player = "O"
    # Or if the current player was O, make it X
    elif current_player == "O":
        current_player = "X"


def check_if_game_over():
    check_winner()
    check_tie()

# Run game of Tic Tac Toe
def play_game():

    # Display initial Game Board.
    display_board()
    # While loop to continue game.
    while in_progress:
        # Processes a user's turn.
        handle_turn(current_player)
        # Check if the game has ended
        check_if_game_over()

        # Switch players.
        flip_player()
        # The game has ended...
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

# Start the game.
play_game()
