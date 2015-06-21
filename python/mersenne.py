#!/usr/bin/env python3
# Fun with Mersenne numbers
# M(n) = 2^n - 1
__package__ = 'raspberrypi'
__author__ = 'zuva.munshi@gmail.com'


def mersenne(n):
    assert isinstance(n, int) and n > 0
    s = 4
    M = 2 ** n - 1
    while n > 2: s, n = ((s * s) - 2) % M, n - 1
    return (M, 'prime' if s == 0 or M < 7 else 'composite')


if __name__ == '__main__':
    import sys

    try:
        n = int(sys.argv[1])
    except:
        n = 1
    m, isprime = mersenne(n)
    print(n, isprime, m)
