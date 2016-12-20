def fibonacci1(n):
    # Write your code here.
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)

def fibonacci2(n):
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
print fibonacci2(39)
print fibonacci1(39)
