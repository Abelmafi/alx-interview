#!/usr/bin/python3
"""defining is_winner function"""


def is_winner(num_rounds, nums):
    """
    Determine the winner of each game in the Prime Number Game.
    Args:
        num_rounds (int): The number of rounds to play.
        nums (list): List of integers representing 'n' for each round.

    Returns:
        str or None: The name of the player with the most wins, or None if the winner cannot be determined.
    """

    def sieve(n):
        """
        Apply the Sieve of Eratosthenes algorithm to generate prime numbers up to 'n'.

        Args:
            n (int): The number to generate prime numbers up to.

        Returns:
            list: A boolean list representing prime numbers up to 'n'.
        """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return primes

    def play_game(n):
        """
        Simulate the game for a given number 'n' and determine the winner.

        Args:
            n (int): The number for the current game.

        Returns:
            str: The name of the winner ('Maria' or 'Ben').
        """
        primes = sieve(n)
        if primes[n]:
            return "Maria"  # Maria wins if 'n' is prime

        largest_prime = 0
        for i in range(n, 1, -1):
            if primes[i]:
                largest_prime = i
                break

        if largest_prime <= 2:
            return "Ben"  # Ben wins if largest prime <= 2

        for i in range(2, largest_prime):
            if primes[i] and play_game(n - i) == "Ben":
                return "Maria"

        return "Ben"

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
