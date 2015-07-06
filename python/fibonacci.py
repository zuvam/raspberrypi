#!/usr/bin/env python3
# Fun with Fibonacci numbers
# Fibonacci Sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# F(1) = 1; F(2) = 1
# F(n) = F(n-1) + F(n-2) , n > 2
__package__ = 'raspberrypi'
__author__ = 'Zuva Munshi, Pranav Munshi'


def fibonacci(n: int) -> [(int, int)]:
    assert isinstance(n, int) and n > 0
    a, b = 0, 1
    for i in range(1, n + 1):
        a, b = b, a + b
        yield i, a


if __name__ == "__main__":
    import sys, time

    x = sys.argv[1] if len(sys.argv) > 1 else input('number: ')
    st = time.time()
    print('First {0} Fibonacci Numbers:'.format(x))
    for n, f in fibonacci(int(x)): print('F({0}) = {1}'.format(n, f))
    print('Calculated in {0} seconds'.format(time.time() - st))
