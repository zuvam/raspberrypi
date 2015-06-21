#!/usr/bin/env python3
# Fun with Mersenne numbers
# M(n) = 2^n - 1
# Lucas–Lehmer primality test for mersenne numbers
# https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test#The_test
# To determine if M(n) = 2^n − 1 is prime
# start with s = 4, M = 2^n -1
# repeat n − 2 times: s = ((s × s) − 2) mod M
# if s = 0 then M is PRIME else COMPOSITE
__package__ = 'raspberrypi'
__author__ = 'zuva.munshi@gmail.com'


def mersenne(x: int) -> (int, str):
    assert isinstance(x, int) and x > 0
    s, M = 4, 2 ** x - 1
    while x > 2: s, x = ((s * s) - 2) % M, x - 1
    return (M, 'prime' if s == 0 or M < 7 else 'composite')


if __name__ == '__main__':
    import sys

    try:
        n = int(sys.argv[1])
    except:
        n = 1
    m, isprime = mersenne(n)
    print(n, isprime, m)
