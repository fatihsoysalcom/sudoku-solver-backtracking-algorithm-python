def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c) # (row, col)
    return None

def is_valid(board, num, pos):
    # Check row
    for c in range(9):
        if board[pos[0]][c] == num and pos[1] != c:
            return False

    # Check column
    for r in range(9):
        if board[r][pos[1]] == num and pos[0] != r:
            return False

    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for r in range(box_y * 3, box_y * 3 + 3):
        for c in range(box_x * 3, box_x * 3 + 3):
            if board[r][c] == num and (r, c) != pos:
                return False
    return True

def solve_sudoku(board):
    find = find_empty(board)
    if not find:
        return True # Base case: no empty cells, puzzle solved

    row, col = find

    for num in range(1, 10): # Try numbers 1 through 9
        if is_valid(board, num, (row, col)):
            board[row][col] = num # Make a choice (tentative assignment)

            # Recursive call: try to solve the rest of the board
            if solve_sudoku(board):
                return True # If this path leads to a solution, propagate True

            # Backtrack: if the recursive call returns False,
            # it means the current 'num' didn't lead to a solution.
            # Reset the cell and try the next number.
            board[row][col] = 0
            
    return False # No number worked for this cell, backtrack further

if __name__ == "__main__":
    example_board = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]

    print("Initial Sudoku Board:")
    print_board(example_board)
    print("\nSolving...\n")

    if solve_sudoku(example_board):
        print("Solved Sudoku Board:")
        print_board(example_board)
    else:
        print("No solution exists for this Sudoku board.")