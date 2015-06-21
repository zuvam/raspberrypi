#!/usr/bin/env python3
# Fun with number caterpillars
# Number caterpillar is chain of numbers from n to 1 such that
# if the number is even the next number is half
# and if the number is odd the next number is plus one
__author__ = 'zuva.munshi@gmail.com'


def caterpillar(n):
    assert isinstance(n, int) and n > 0
    c = [n]
    while n > 1:
        if (n % 2 == 0):
            n = n / 2
        else:
            n = n + 1
        c.append(n)
    return c


if __name__ == '__main__':
    import sys

    try:
        n = int(sys.argv[1])
    except:
        n = 1
    c = caterpillar(n)
    print(n, len(c), c)
