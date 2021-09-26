## Requirements: ##
# 1. Game Board
# 2. Display board
# 3. play game
# 4. handle turn 
# 5. check win
 # 5.1.check rows
 # 5.2 check columns
 # 5.3 check diagonals
# 6. check tie
# 7. flip player

# -- Global Variables --#

#  Game Board
board = ["-","-","-",
        "-","-","-",
        "-","-","-",]

# if game_still_going
game_still_going = True

# Who won? or tie?
winner = None

# Whos turn is it  
current_player = 'X'


# -- Functions -- #

# Display Board
def display_board():
  print(board[0]+" | "+board[1]+" | "+board[2])
  print(board[3]+" | "+board[4]+" | "+board[5])
  print(board[6]+" | "+board[7]+" | "+board[8])


# Play game of Tic Tac Toe
def play_game():

  #Display initial board
  display_board()

  # While the game is still going
  while game_still_going:

    # handle a single turn of an arbitiary player
    handle_turn(current_player)

    # check if game has ended
    check_if_game_over()

    # Flip to the other player
    flip_player()
  
  #The game has ended
  if winner == 'X' or winner == 'O':
    print(winner+" Won")
  elif winner == None:
    print("Tie")


# Handle a single turn of an arbitary player
def handle_turn(player):

  print(player+"'s turn")
  position = input("Choose a position from 1-9: ")
  
  valid = False
  while not valid:
    while position not in ["1","2","3", "4","5","6","7","8","9"]:
      position = input("Invalid input. Choose a position from 1-9: ")

    # -1 because user is entering input from 1 but index starts from 0 or 1 less
    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  board[position] = player
  display_board()


def check_if_game_over():
  check_if_winner()
  check_if_tie()


def check_if_winner():

  # Set up global variable
  global winner

  # check rows
  row_winner = check_rows() 
  # check columns 
  column_winner = check_columns()
  # check diagonals 
  diagonal_winner = check_diagonals()

 # Get winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  
  return
 

def check_rows():

  global game_still_going

  #check if any of the rows have all same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  
  # if any row have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  
  # return the winner (X or O)
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  
  return 


def check_columns():

  global game_still_going

  #check if any of the columns have all same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  
  # if any columns have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  
  # return the winner (X or O)
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]

  return


def check_diagonals():

  global game_still_going

  #check if any of the diagonals have all same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  
  # if any diagonals have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  
  # return the winner (X or O)
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]

  return


def check_if_tie():
  global game_still_going

  if "-" not in board:
    game_still_going = False

  return


def flip_player():

  global current_player

  #if current player was X, then change to O
  if current_player == "X":
    current_player = "O"
  #ifcurrent player was O, then change to X
  elif current_player == "O":
    current_player = "X"

  return

  
play_game()