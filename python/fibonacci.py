#!/usr/bin/env python3
# Fun with Fibonacci numbers
# Fibonacci Sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# F(1) = 1; F(2) = 1
# F(n) = F(n-1) + F(n-2) , n>2
__package__ = 'raspberrypi'
__author__ = 'zuva.munshi@gmail.com'


def fibonacci(n):
    assert isinstance(n, int) and n > 1
    fm, fn = 1, 1
    while n > 2: fm, fn, n = fn, fm + fn, n - 1
    return fn


if __name__ == '__main__':
    import sys

    try:
        n = int(sys.argv[1])
    except:
        n = 1
    f = fibonacci(n)
    print(n, len(str(f)), f)
