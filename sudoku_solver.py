import random
import copy

# solving the board for right solution
def find_empty(board):
    """find the row, col that still have empty cell"""
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None, None 

def is_valid(board, guess, row, col):
    """check if the guess is right or not and return True or False"""
    row_vals = board[row]
    for val in row_vals: 
        if val == guess:
            return False 
    
    col_vals = []
    for i in range(9):
        col_vals.append(board[i][col])   
    if guess in col_vals:
        return False
    
    
    row_square = 3 * (row // 3)
    col_square = 3 * (col // 3)
    
    for r in range(row_square, row_square + 3):
        for c in range(col_square, col_square + 3):
            if board[r][c] == guess:
                return False
    return True 

def sudoku_solver(board):
    """using bactracking to solve a sudoku puzzle"""
    row, col = find_empty(board)
    if row is None:
        return True 
    
    for guess in range(10): 
        if is_valid(board, guess, row, col): 
            board[row][col] = guess            
            if sudoku_solver(board):
                return True
        board[row][col] = 0 
    return False


# Generate the board
def generate_full_board():
    '''create a board'''
    board = []
    for i in range(9):
        row = []
        for i in range(9):
            row.append(0)
        board.append(row)
    sudoku_solver(board)
    return board

def make_puzzle(board, clues=35):
    '''make a puzzle'''
    puzzle = copy.deepcopy(board)
    cells = []
    for r in range(9):
        for c in range(9):
            cells.append((r, c))
    random.shuffle(cells)
    to_remove = 81 - clues
    for i in range(to_remove):
        r, c = cells[i]
        puzzle[r][c] = 0
    return puzzle

def print_board(board):
    '''printing the board'''
    column_header = "    "
    for c in range(9):
        column_header += str(c) + " "
    print(column_header.rstrip())
    print("  " + "-" * 21)

    for i in range(9):
        row = board[i]
        row_str = str(i) + " | "
        for num in row:
            if num != 0:
                row_str += str(num) + " "
            else:
                row_str += ". "
        print(row_str.rstrip())
        if i % 3 == 2 and i != 8:
            print("  " + "-" * 21)


def check_guess(solution, board, row, col, guess):
    '''check the guess is right or not'''
    if solution[row][col] == guess:
        board[row][col] = guess
        return True
    return False

def is_complete(board):
    '''check if the board is complete or not'''
    for row in board:
        for cell in row:
            if cell == 0:
                return False
    return True
#Create the game

def play_sudoku():
    '''taking user input and solve the puzzle'''
    solution = generate_full_board()
    puzzle = make_puzzle(solution, clues=35)
    print("Welcome to the Sudoku game")
    print("Rule: You must enter your guesses in this format: row col value (e.g. 0 1 5)")
    print_board(puzzle)

    while not is_complete(puzzle):
        try:
            player_input = input("Your move (row col value): ")
            if player_input.lower() in ("quit", "exit"):
                print("Quitting the game")
                return
            row, col, val = map(int, player_input.strip().split())
            if not (0 <= row < 9 and 0 <= col < 9 and 1 <= val <= 9):
                print("Invalid input. Use numbers: row 0-8, col 0-8, value 1-9.")
                continue
            if puzzle[row][col] != 0:
                print("Cell is already filled.")
                continue
            if check_guess(solution, puzzle, row, col, val):
                print("Correct! Updated board:")
                print_board(puzzle)
            else:
                print("Wrong guess. Try again.")
        except ValueError:
            print("Please enter three numbers separated by spaces (e.g., 0 1 5).")

    print("Congratulations! You solved the puzzle!")

if __name__ == '__main__':
    play_sudoku()