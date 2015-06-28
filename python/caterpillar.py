#!/usr/bin/env python3
# Fun with number caterpillars
# Number caterpillar is chain of numbers from n to 1 such that
# if number is even the next number is half
# and if number is odd the next number is plus one
# caterpillar(17) = [17, 18, 9, 10, 5, 6, 3, 4, 2, 1]
__package__ = 'raspberrypi'
__author__ = 'zuva.munshi@gmail.com'


def caterpillar(n: int) -> [int]:
    assert isinstance(n, int) and n > 0
    nc = [n]
    while n > 1:
        n = int(n / 2) if (n % 2 == 0) else n + 1
        nc.append(n)
    return nc


if __name__ == '__main__':
    import sys, time

    x = sys.argv[1] if len(sys.argv) > 1 else input('number: ')
    st = time.time()
    c = caterpillar(int(x))
    print('Number: {0}; Caterpillar Length: {1}; Caterpillar: {2}'.format(x, len(c), '->'.join(str(n) for n in c)))
    print('Calculated in {0} seconds'.format(time.time() - st))
