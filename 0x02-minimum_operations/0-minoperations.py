#!/usr/bin/python3
""" min operaions """


def minOperations(n):
    """It takes an integer n as input and returns an integer that represents
    the minimum number of operations required to reach n H characters
    in the file."""
    if not isinstance(n, int) or n <= 1:
        return 0
    if n == 2:
        return 2
    count = 0
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                count += i
                n //= i
                break
    return count
