# Sudoku Game

Welcome to the Sudoku Game repository! This project provides an interactive console-based Sudoku game where users can guess numbers for an unsolved Sudoku puzzle. The game will check if the guesses are correct and provide real-time feedback. Once all cells are correctly filled, the game is complete.

## Features

* **Sudoku Puzzle Generation:** The game generates a valid Sudoku board and removes some numbers to create a puzzle.
* **Interactive Guessing:** Players can enter guesses for any empty cell, and the game will verify whether the guess is correct.
* **Real-Time Feedback:** After each guess, the game provides feedback on whether the guess was correct or incorrect, along with the updated board.
* **Simple Controls:** The game can be controlled entirely through the console, with easy-to-follow input instructions.

## Gameplay Instructions

1. **Starting the Game:** After running the program, you'll be prompted with an unsolved Sudoku puzzle where some numbers are missing (represented by `.`).
2. **Making a Guess:** To make a guess, input the row, column, and value in the format:

   ```
   row col value
   ```

   For example, entering `0 2 4` will place the number `4` in row `0`, column `2`.
3. **Feedback:** After each guess, the game will inform you if your guess was correct or not and display the updated puzzle.
4. **Finish the Game:** The game continues until all empty cells are filled correctly, at which point you are congratulated for solving the puzzle.

## Algorithm

### Puzzle Generation

1. **Solving the Puzzle:** The algorithm first generates a full valid Sudoku board using a **backtracking algorithm**. This algorithm systematically tries numbers in empty cells and backtracks if it encounters a conflict (i.e., the number does not fit the Sudoku constraints).

2. **Creating the Puzzle:** Once a valid complete board is generated, the algorithm removes numbers to create a puzzle. The number of clues (pre-filled numbers) is customizable (by default, the game leaves 35 clues). This creates the puzzle that players will solve.

### Backtracking Algorithm

The **backtracking algorithm** is used to fill the Sudoku board. It works as follows:

1. Find an empty cell.
2. Try placing a valid number (1-9) in that cell.
3. Check if the number is valid by ensuring it does not already exist in:

   * The row.
   * The column.
   * The 3x3 subgrid.
4. If the number is valid, place it in the cell and recursively try to fill the next empty cell.
5. If placing the number leads to a dead end (i.e., no valid numbers can be placed), backtrack by removing the number and trying the next possibility.
6. The algorithm continues until the board is completely filled with valid numbers.

### Puzzle Solving

Once the game starts, players make guesses for the empty cells. For each guess:

1. The program checks if the player's guess matches the correct value for that cell.
2. If the guess is correct, the number is filled into the board, and the updated board is displayed.
3. If the guess is incorrect, the game prompts the player to try again.

This simple feedback loop continues until the player has correctly solved the puzzle by filling all the empty cells.

## Code Structure

* `generate_full_board()`: Uses backtracking to generate a complete valid Sudoku board.
* `make_puzzle()`: Randomly removes numbers from the full board to create a solvable puzzle.
* `print_board()`: Displays the current state of the puzzle in a readable format with row and column labels.
* `check_guess()`: Validates a player's guess by comparing it to the correct solution.
* `is_complete()`: Checks if the board is completely solved (i.e., all cells are filled).
* `play_sudoku()`: Controls the gameplay by allowing the player to input guesses and displaying real-time feedback.

## Requirements

* Python 3.x
* No external libraries required.

## How to Run

1. Clone the repository:

   ```
   git clone https://github.com/AnVu1408/Sudoku-Game.git
   ```
2. Navigate to the project directory:

   ```
   cd Sudoku-Game
   ```
3. Run the Python script:

   ```
   python sudoku_game.py
   ```

### Additional Notes

* The game is designed to be a fun way to practice Sudoku skills, but it also demonstrates how backtracking algorithms can be applied to solve constraint satisfaction problems like Sudoku.
* Feel free to modify the difficulty by changing the number of pre-filled clues or adjusting the backtracking algorithm's settings.
