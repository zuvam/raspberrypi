#!/usr/bin/env python3
# Fun with Fibonacci numbers
# Fibonacci Sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# F(1) = 1; F(2) = 1
# F(n) = F(n-1) + F(n-2) , n > 2
__package__ = 'raspberrypi'
__author__ = 'zuva.munshi@gmail.com'


def fibonacci(x: int) -> int:
    assert isinstance(x, int) and x > 0
    a, b = 1, 1
    while x > 2: a, b, x = b, a + b, x - 1
    return b


if __name__ == '__main__':
    import sys

    try:
        n = int(sys.argv[1])
    except:
        n = 1
    f = fibonacci(n)
    print(n, len(str(f)), f)
