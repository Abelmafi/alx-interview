#!/usr/bin/python3
'''Task 1: '''


def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        num = total // coin

        total -= num * coin
        num_coins += num

        if total == 0:
            return num_coins
    return -1
