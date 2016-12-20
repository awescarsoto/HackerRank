'''
Davis has  staircases in his house and he likes to climb each staircase , , or  steps at a time. Being a very precocious child, he wonders how many ways there are to reach the top of the staircase.

Given the respective heights for each of the  staircases in his house, find and print the number of ways he can climb each staircase on a new line.

Input Format

The first line contains a single integer, , denoting the number of staircases in his house.
Each line  of the  subsequent lines contains a single integer, , denoting the height of staircase .

Constraints

Subtasks

 for  of the maximum score.
Output Format

For each staircase, print the number of ways Davis can climb it in a new line.

Sample Input

3
1
3
7
Sample Output

1
4
44
Explanation

Let's calculate the number of ways of climbing the first two of the Davis'  staircases:

The first staircase only has  step, so there is only one way for him to climb it (i.e., by jumping  step). Thus, we print  on a new line.
The second staircase has  steps and he can climb it in any of the four following ways:
Thus, we print  on a new line.
'''


def find_ways(n, ways):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif ways[n] == 0:
        ways[n] = find_ways(n - 1, ways) + find_ways(n - 2, ways) + find_ways(n - 3, ways)
    return ways[n]


s = int(raw_input().strip())
ways = [0] * 37
for a0 in xrange(s):
    n = int(raw_input().strip())
    find_ways(n, ways)
    print str(ways[n])