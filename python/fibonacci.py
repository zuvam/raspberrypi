#!/usr/bin/env python3
# Fun with Fibonacci numbers
# Fibonacci Sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# F(1) = 1; F(2) = 1
# F(n) = F(n-1) + F(n-2) , n>2
def fibonacci(n):
    assert n > 0
    if n < 3:
        return 1
    else:
        fm, fn = 1, 1
        for x in range(2, n): fm, fn = fn, fm + fn
        return fn


if __name__ == '__main__':
    import sys

    try:
        n = int(sys.argv[1])
    except:
        n = 1
    print(n, fibonacci(n))
