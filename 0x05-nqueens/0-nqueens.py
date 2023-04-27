#!/usr/bin/python3
"""Python n-queens solver"""
import sys


def is_safe(board, row, col):
    """Return True if it's safe to place a queen at board[row][col]
    else False."""
    # Check row
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower diagonal
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def nqueens(board, col, solutions):
    """Recursively solve the n-queens problem."""
    if col == len(board):
        # All queens have been placed
        solution = []
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == 1:
                    solution.append([row, col])
        solutions.append(solution)
    else:
        for row in range(len(board)):
            if is_safe(board, row, col):
                board[row][col] = 1
                nqueens(board, col + 1, solutions)
                board[row][col] = 0


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for i in range(n)]
    solutions = []
    nqueens(board, 0, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
