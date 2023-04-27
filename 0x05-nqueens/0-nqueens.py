#!/usr/bin/python3
"""Python n-queens solver"""
import sys


def nqueens(N):
    """Solves the board"""
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [[0 for x in range(N)] for y in range(N)]

    # Try to place a queen in each column
    solve(board, 0, N)


def solve(board, col, N):
    """Base case: all queens have been placed"""
    if col == N:
        print_board(board)
        return True

    # Try to place a queen in each row of the current column
    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve(board, col + 1, N)
            board[row][col] = 0

    return False


def is_safe(board, row, col):
    """check if its save or not"""
    N = len(board)

    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def print_board(board):
    """print the board"""
    N = len(board)
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


if __name__ == "__main__":
    """main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)
