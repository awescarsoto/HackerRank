'''
Given a number of dollars, , and a list of dollar values for  distinct coins, , find and print the number of different ways you can make change for  dollars if each coin is available in an infinite quantity.

Hints:

You can solve this problem recursively, but you must optimize your solution to eliminate overlapping subproblems using Dynamic Programming if you wish to pass all test cases. More specifically, think of ways to store the checked solutions and use the stored values to avoid repeatedly calculating the same values.
Think about the degenerate cases:
How many ways can you make change for  dollars?
How many ways can you make change for less than  dollars if you have no coins?
If you are having trouble defining the storage for your precomputed values, then think about it in terms of the base case .
Input Format

The first line contain two space-separated integers describing the respective values of  and .
The second line contains  space-separated integers describing the respective values of , where each integer denotes the dollar value of a distinct coin available in an infinite quantity.

Constraints

The list of coins contains  distinct integers where each integer denotes the dollar value of a coin available in an infinite quantity.
Output Format

Print a single integer denoting the number of ways we can make change for  dollars using an infinite supply of our  types of coins.

Sample Input 0

4 3
1 2 3
Sample Output 0

4
Explanation 0
For  and  there are four solutions:

Thus, we print  on a new line.

Sample Input 1

10 4
2 5 3 6
Sample Output 1

5
Explanation 1
For  and  there are five solutions:

Thus, we print  on a new line.
'''

# !/bin/python

import sys


def make_change(coins, n):
    counts = [0] * (n + 1)
    # sorted(coins)
    for i in range(0, n + 1, coins[0]):
        counts[i] = 1
    for i in range(1, len(coins)):  # Go through rest of coins
        coin = coins[i]
        for j in range(coin, n + 1):
            difference = j - coin
            if difference == 0:
                counts[j] += 1
            else:
                counts[j] += counts[difference]
    return counts[n]


n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
coins = map(int, raw_input().strip().split(' '))
print make_change(coins, n)
