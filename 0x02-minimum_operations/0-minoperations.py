#!/usr/bin/python3
""" min operaions """


def minOperations(n):
    """It takes an integer n as input and returns an integer that represents
    the minimum number of operations required to reach n H characters
    in the file."""
    if n <= 1:
        return 0
    if n % 2 == 1:
        return 0
    else:
        return minOperations(n // 2) + 2
