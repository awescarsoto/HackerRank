'''
A prime is a natural number greater than  that has no positive divisors other than  and itself. Given  integers, determine the primality of each integer and print whether it is Prime or Not prime on a new line.

Note: If possible, try to come up with an  primality algorithm, or see what sort of optimizations you can come up with for an  algorithm. Be sure to check out the Editorial after submitting your code!

Input Format

The first line contains an integer, , denoting the number of integers to check for primality.
Each of the  subsequent lines contains an integer, , you must test for primality.

Constraints

Output Format

For each integer, print whether  is Prime or Not prime on a new line.

Sample Input

3
12
5
7
Sample Output

Not prime
Prime
Prime
Explanation

We check the following  integers for primality:

 is divisible by numbers other than  and itself (i.e.: , , ), so we print Not prime on a new line.
 is only divisible  and itself, so we print Prime on a new line.
 is only divisible  and itself, so we print Prime on a new line.
'''

from math import sqrt

p = int(raw_input().strip())
for _ in xrange(p):
    n = int(raw_input().strip())
    if n < 2:
        print "Not prime"
        continue
    prime = True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            print "Not prime"
            prime = False
            break
    if prime == True:
        print "Prime"
