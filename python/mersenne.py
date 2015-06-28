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
__author__ = 'Zuva Munshi'


def mersenne(n: int, primes=False) -> [(int, int)]:
    assert isinstance(n, int) and n > 0
    M = 0
    for i in range(1, n + 1):
        M = (2 * M) + 1
        if primes:
            s = 4 if i > 2 else 0
            for j in range(0, i - 2): s = ((s * s) - 2) % M
            if s == 0: yield i, M
        else:
            yield i, M


if __name__ == '__main__':
    import sys, time

    x = sys.argv[1] if len(sys.argv) > 1 else input('number: ')
    st = time.time()
    print('Primes in First {0} Mersenne Numbers:'.format(x))
    for n, M in mersenne(int(x), True): print('M({0}) = {1}'.format(n, M))
    print('Calculated in {0} seconds'.format(time.time() - st))
