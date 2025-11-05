def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print()


def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    # Base case: all queens placed
    if row == n:
        print_board(board)
        return True

    found = False
    # Try placing queen in each column
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, row + 1, n):
                found = True
            board[row][col] = 0  # backtrack

    return found


# ---- Driver Code ----
n = int(input("Enter the number of queens: "))

# Step 1: Create board and place first queen
board = [[0 for _ in range(n)] for _ in range(n)]
first_row = 0
first_col = int(input(f"Enter column (0 to {n-1}) for first queen in row 0: "))
board[first_row][first_col] = 1

# Step 2: Solve from next row
if not solve_n_queens(board, first_row + 1, n):
    print("No solution exists with the first queen placed there.")
