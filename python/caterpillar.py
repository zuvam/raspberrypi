#!/usr/bin/env python3
# Fun with number caterpillars
# Number caterpillar is chain of numbers from n to 1 such that
# if number is even the next number is half
# and if number is odd the next number is plus one
# caterpillar(17) = [17, 18, 9, 10, 5, 6, 3, 4, 2, 1]
__package__ = 'raspberrypi'
__author__ = 'zuva.munshi@gmail.com'


def caterpillar(x: int) -> [int]:
    assert isinstance(x, int) and x > 0
    nc = [x]
    while x > 1:
        x = int(x / 2) if (x % 2 == 0) else x + 1
        nc.append(x)
    return nc


if __name__ == '__main__':
    import sys

    try:
        n = int(sys.argv[1])
    except:
        n = 1
    c = caterpillar(n)
    print(n, len(c), c)
