'''
Consider an array of  integers, , where all but one of the integers occur in pairs. In other words, every element in  occurs exactly twice except for one unique element.

Given , find and print the unique element.

Input Format

The first line contains a single integer, , denoting the number of integers in the array.
The second line contains  space-separated integers describing the respective values in .

Constraints

It is guaranteed that  is an odd number.
, where .
Output Format

Print the unique number that occurs only once in  on a new line.

Sample Input 0

1
1
Sample Output 0

1
Explanation 0
The array only contains a single , so we print  as our answer.

Sample Input 1

3
1 1 2
Sample Output 1

2
Explanation 1
We have two 's and one . We print , because that's the only unique element in the array.

Sample Input 2

5
0 0 1 2 1
Sample Output 2

2
Explanation 2
We have two 's, two 's, and one . We print , because that's the only unique element in the array.
'''

#!/bin/python

import sys

def lonely_integer(a):
    answer = 0
    for integer in a:
        answer = answer ^ integer
    return answer

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)