import numpy as np

def possible(sudoku_puzzle, Row, Column, Num):
    # Is the Num appearing in the given Row?
    for i in range(0, 9):
        if sudoku_puzzle[Row][i] == Num:
            return False

    # Is the Num appearing in the given Column?
    for i in range(0, 9):
        if sudoku_puzzle[i][Column] == Num:
            return False

    # Is the Num appearing in the given square?
    x0 = (Column // 3) * 3
    y0 = (Row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku_puzzle[y0+i][x0+j] == Num:
                return False

    return True

def solution(sudoku_puzzle):
    for Row in range(0, 9):
        for Column in range(0, 9):
            if sudoku_puzzle[Row][Column] == 0:
                for Num in range(1, 10):
                    if possible(sudoku_puzzle, Row, Column, Num):
                        sudoku_puzzle[Row][Column] = Num
                        solution(sudoku_puzzle)
                        sudoku_puzzle[Row][Column] = 0

                return

    print(np.matrix(sudoku_puzzle))
    input('More possible solutions')

if __name__ == "__main__":
    # Take user input for Sudoku puzzle
    sudoku_puzzle = []
    for i in range(9):
        row = list(map(int, input(f"Enter row {i + 1} (use 0 for empty cells): ").split()))
        sudoku_puzzle.append(row)

    solution(sudoku_puzzle)
