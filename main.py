import random

EMPTY_SLOT = "-"
X_PLAYER = "X"
O_PLAYER = "0"
TIE = "tie"

WIN_COMBINATION_INDICES = [
  # Complete row
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  # Complete column
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  # Complete diagonal
  [0, 4, 8],
  [2, 4, 6]
]


def initialize_board():
  board = [EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT,
            EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT,
            EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT]
  return board


def display_board(board):
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


def handle_turn(player, board):
  print(f"{player}, it's your turn.")
  handle_the_turn = False
  
  while handle_the_turn ==False:
    position = input("Please choose an available number on the board from 1-9: ") # TODO Ask player to input a position (1-9). Ask while the position is not valid (check using valid_position)
    
    if position not in ["1","2","3","4","5","6","7","8","9"]:
      print("Invalid input! Please choose an available number in the board from 1-9: ")
   
    else:
      position = int(position) - 1
      if board[position]!= EMPTY_SLOT:
        print("The selected number is not available!")
    
      else:
        handle_the_turn = True
  
  board[position] = player # TODO Write player's sign in 
  return board
    
    
def switch_player(player):
  if player == X_PLAYER:# TODO Switch the player: X --> 0 or 0 --> X
    player = O_PLAYER
  
  else: #player == O_PLAYER:
    player = X_PLAYER

  return player


def check_for_winner(board):
  winner = None
  filled_slots = 0
  
  WIN_COMBINATION_INDICES[0][0]=WIN_COMBINATION_INDICES[3][0]=WIN_COMBINATION_INDICES[6][0]= board[0]
  WIN_COMBINATION_INDICES[0][1]=WIN_COMBINATION_INDICES[4][0]=board[1]
  WIN_COMBINATION_INDICES[0][2]=WIN_COMBINATION_INDICES[5][0]=WIN_COMBINATION_INDICES[7][0]=board[2]
  WIN_COMBINATION_INDICES[1][0]=WIN_COMBINATION_INDICES[3][1]=board[3]
  WIN_COMBINATION_INDICES[1][1]=WIN_COMBINATION_INDICES[4][1]=WIN_COMBINATION_INDICES[6][1]=WIN_COMBINATION_INDICES[7][1]=board[4]
  WIN_COMBINATION_INDICES[1][2]=WIN_COMBINATION_INDICES[5][1]=board[5]
  WIN_COMBINATION_INDICES[2][0]=WIN_COMBINATION_INDICES[3][2]=WIN_COMBINATION_INDICES[7][2]=board[6]
  WIN_COMBINATION_INDICES[2][1]=WIN_COMBINATION_INDICES[4][2]=board[7]
  WIN_COMBINATION_INDICES[2][2]=WIN_COMBINATION_INDICES[5][2]=WIN_COMBINATION_INDICES[6][2]=board[8]
  
  # TODO Check if any of the players got a win combination
  for i in WIN_COMBINATION_INDICES:# Hint: loop over WIN_COMBINATION_INDICES to check if one of the combination is X-X-X or O-O-O
    if i[0]==i[1]==i[2]==X_PLAYER:
      winner=X_PLAYER
      
    elif i[0]==i[1]==i[2]==O_PLAYER:
      winner=O_PLAYER

    elif EMPTY_SLOT not in board and not winner:# TODO If there is no winner, check if all spots are filled already. This would mean tie (winner = TIE)
      winner = TIE
  # Hint: count number of filled slots

  return winner

def player_random(): # TODO (optional): select who starts randomly --> do this in a separate function
  player = random.choice([X_PLAYER,O_PLAYER])
  return player
  
def tic_tac_toe():
  winner = None
  game_still_going = True
  player = player_random() 
  # Initialize board
  board = initialize_board()

  while game_still_going:# TODO run this while the game is still going
      # Display board
      display_board(board)

      # Ask the player for a valid position and write it on the board
      player = switch_player(player) 
      
      board = handle_turn(player, board)

      # Check if there is a winner already
      winner = check_for_winner(board)

      if winner:# TODO stop the game if there is a winner, otherwise switch the player
        game_still_going = False

  print("THE END")
  if winner == TIE:
      print("Tie")
  else:
      print(f"Congratulations {winner}!!")
  display_board(board)


# Start game
tic_tac_toe()
