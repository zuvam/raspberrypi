#!/usr/bin/env python3
# Fun with Mersenne numbers
# M(n) = 2^n - 1
__package__ = 'raspberrypi'
__author__ = 'zuva.munshi@gmail.com'


def mersenne(n):
    assert isinstance(n, int) and n > 1
    return 2 ** n - 1


if __name__ == '__main__':
    import sys

    try:
        n = int(sys.argv[1])
    except:
        n = 1
    m = mersenne(n)
    print(n, m)
