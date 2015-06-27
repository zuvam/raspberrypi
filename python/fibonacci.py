#!/usr/bin/env python3
# Fun with Fibonacci numbers
# Fibonacci Sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# F(1) = 1; F(2) = 1
# F(n) = F(n-1) + F(n-2) , n > 2
__package__ = 'raspberrypi'
__author__ = 'Zuva Munshi, Pranav Munshi'


def fibonacci(x: int) -> [(int, int)]:
    assert isinstance(x, int) and x > 0
    a, b = 0, 1
    for n in range(1, x + 1):
        a, b = b, a + b
        yield n, a


if __name__ == '__main__':
    import sys

    x = sys.argv[1] if len(sys.argv) > 1 else input('number: ')
    for n, f in fibonacci(int(x)): print(n, f)
