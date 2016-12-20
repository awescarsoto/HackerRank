'''
The Fibonacci Sequence
The Fibonacci sequence begins with  and  as its respective first and second terms. After these first two elements, each subsequent element is equal to the sum of the previous two elements.

Here is the basic information you need to calculate :

Task
Given , complete the fibonacci function so it returns .

Input Format

Locked stub code in the editor reads a single integer denoting the value of  and passes it to the fibonacci function.

Constraints

Output Format

Locked stub code in the editor prints the value of  returned by the fibonacci function.

Sample Input

3
Sample Output

2
Explanation

Consider the Fibonacci sequence:
...

We want to know the value of . If we look at the sequence above,  evaluates to . Thus, we print  as our answer.
'''

def fibonacci(n):
    # Write your code here.
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        temp1 = 0
        temp2 = 1
        for i in range(2, n + 1):
            fib = temp1 + temp2
            temp1 = temp2
            temp2 = fib
        return fib
n = int(raw_input())
print(fibonacci(n))