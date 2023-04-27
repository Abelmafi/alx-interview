N Queens Problem Solver

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.

This program solves the N queens problem by printing every possible solution to the problem. The program takes a single command-line argument, the size of the chessboard N.
Usage

To run the program, use the following command:

mathematica

python nqueens.py N

where N is an integer greater or equal to 4.

If the user called the program with the wrong number of arguments, the program prints the message:

makefile

Usage: nqueens N

and exits with the status 1.

If N is not an integer, the program prints the message:

css

N must be a number

and exits with the status 1.

If N is smaller than 4, the program prints the message:

mathematica

N must be at least 4

and exits with the status 1.
Output

The program prints every possible solution to the N queens problem, one solution per line. Each solution is represented as an N×N chessboard with the queens represented by 'Q' characters and the empty squares represented by '.' characters. For example, the following is a solution for N=4:

css

. Q . .
. . . Q
Q . . .
. . Q .

The solutions are printed in no particular order.
Implementation

The program is implemented in Python 3 and only imports the sys module. The program uses a recursive algorithm to try to place a queen in each column of the chessboard. For each column, the program tries to place a queen in each row of the column. If a queen can be placed in a given row without attacking any other queens, the program recursively calls itself to try to place queens in the remaining columns. If all queens have been placed, the program prints the current state of the chessboard as a solution to the problem.

The program uses a helper function is_safe() to check if a queen can be placed in a given row and column without attacking any other queens. This function checks if there are any other queens on the same row, upper diagonal, or lower diagonal.

The program uses a helper function print_board() to print the current state of the chessboard as a solution.
