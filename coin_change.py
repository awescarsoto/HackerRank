#!/bin/python

import sys


def make_change(coins, n):
    ways = [0] * (n + 1)  # Initialize all values up to our dollar max with 0s
    # sorted(coins)
    for i in range(0, n + 1, coins[0]):  # Set all multiples of 1st coin to 1 way
        ways[i] = 1
    for i in range(1, len(coins)):  # Go through rest of coins
        coin = coins[i]
        for j in range(coin, n + 1):  # Go through rest of dollar values starting at coin's value
            difference = j - coin  # Figure out difference needed to make dollar amount
            if difference == 0:  # Special case where the coins is the same as dollar amount
                ways[j] += 1
            else:  # Adds in the ways the difference could be made
                ways[j] += ways[difference]
    return ways[n]


n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
coins = map(int, raw_input().strip().split(' '))
print make_change(coins, n)
