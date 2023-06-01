#!/usr/bin/python3
'''Prime Game'''


def isWinner(x, nums):
    """
    Determine the winner of each game in the Prime Number Game.

    Args:
        x (int): The number of rounds to play.
        nums (list): List of integers representing 'n' for each round.

    Returns:
        str or None: The name of the player with the most wins, or None if the winner cannot be determined.
    """
    def is_round_winner(n):
        """
        Find the winner of a round.

        Args:
            n (int): The value of 'n' for the round.

        Returns:
            str or None: The name of the round winner ('Maria' or 'Ben'), or None if the round is a draw.
        """
        number_list = [i for i in range(1, n + 1)]
        players = ['Maria', 'Ben']

        for i in range(n):
            current_player = players[i % 2]
            selected_idxs = []
            prime = -1

            for idx, num in enumerate(number_list):
                if prime != -1:
                    if num % prime == 0:
                        selected_idxs.append(idx)
                else:
                    if is_prime(num):
                        selected_idxs.append(idx)
                        prime = num

            if prime == -1:
                if current_player == players[0]:
                    return players[1]
                else:
                    return players[0]
            else:
                for idx, val in enumerate(selected_idxs):
                    del number_list[val - idx]

        return None

    def is_prime(n):
        """
        Check if a number is prime.

        Args:
            n (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
            return False
        else:
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

    winner_counter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        round_winner = is_round_winner(nums[i])
        if round_winner is not None:
            winner_counter[round_winner] += 1

    if winner_counter['Maria'] > winner_counter['Ben']:
        return 'Maria'
    elif winner_counter['Ben'] > winner_counter['Maria']:
        return 'Ben'
    else:
        return None
