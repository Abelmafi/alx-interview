#!/usr/bin/python3
"""defining is_winner function"""


def isWinner(x, nums):
    """
    Determine the winner of each game in the Prime Number Game.

    Args:
        x (int): The number of rounds to play.
        nums (list): List of integers representing 'n' for each round.

    Returns:
        str or None: The name of the player with the most wins, or None if the winner cannot be determined.
    """

    def is_prime(n):
        """
        Check if a number is prime.

        Args:
            n (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(is_prime(i) for i in range(1, n + 1))
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
