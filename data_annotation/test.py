import random

#Let's create a 2D list to represent our game board
board = [['O' for x in range(7)] for y in range(7)]

def print_board(board):
    for row in board:
        print(' '.join(row))

print_board(board)

# Let's have some ships
num_of_ships = 3
ship_length = 3
# We need 2 dictionary one for storing ships and other for uncovered coordinates
ships = {}
coordinates_uncovered = {}


def place_ship(board, ships, ship_length):
    for ship in range(num_of_ships):
        ship_status = []
        while True:
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board[0]) - ship_length)
            # Check if the ship can be placed at this position
            vertical = random.randint(0, 1) == 0
            if vertical:
                for i in range(ship_length):
                    if board[row + i][col] == 'O':
                        break
                else:
                    ship_status.extend([(row + i, col) for i in range(ship_length)])
                    break
            else:
                for j in range(ship_length):
                    if board[row][col + j] == 'O':
                        break
                else:
                    ship_status.extend([(row, col + j) for j in range(ship_length)])
                    break

        if len(ship_status) == ship_length:
            ships[ship] = ship_status
            for coor in ship_status:
                board[coor[0]][coor[1]] = 'S'
                coordinates_uncovered[coor] = 'S'
            break


place_ship(board, ships, ship_length)
print_board(board)

def user_input_guess(board):
    while True:
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))
        if guess_row < 0 or guess_row >= len(board) or guess_col < 0 or guess_col >= len(board[0]):
            print("Invalid input. Please guess within the range of the board.")
        else:
            return guess_row, guess_col


def reveal_ship(guess_row, guess_col, board, coordinates_uncovered):
    if (guess_row, guess_col) in coordinates_uncovered:
        print("You have already guessed this coordinate.")
    else:
        if board[guess_row][guess_col] == 'S':
            coordinates_uncovered[guess_row, guess_col] = 'S'
            print("Hit!")
        else:
            coordinates_uncovered[guess_row, guess_col] = 'X'
            print("Miss!")


def game_still_active(ships):
    for ship in ships.values():
        if any('S' in coordinate for coordinate in ship):
            return True
    return False


import random

# Let's create a 2D list to represent our game board: size 5x5
board_size = 5
board = [['O' for x in range(board_size)] for y in range(board_size)]

num_of_ships = 3
ship_length = 3
ships = {}
coordinates_uncovered = {}



def game_loop():
    place_ship(board, ships, ship_length)
    print_board(board)
    while True:
        guess_row, guess_col = user_input_guess(board)
        reveal_ship(guess_row, guess_col, board, coordinates_uncovered)
        print_board(board)

        if not game_still_active(ships):
            print("You Win!!")
            break
        # It's computer's turn now:
        # (For simplicity, we will randomly guess)
        computer_guess_row = random.randint(0, board_size - 1)
        computer_guess_col = random.randint(0, board_size - 1)
        reveal_ship(computer_guess_row, computer_guess_col, board, coordinates_uncovered)

        if not game_still_active(ships):
            print("Computer Wins!!")
            break

game_loop()