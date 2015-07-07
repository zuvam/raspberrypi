#!/usr/bin/env python3
# Solutions to Project Euler Problems
# About Project Euler: https://projecteuler.net
# List of Problems: https://projecteuler.net/archives
__author__ = 'Zuva Munshi'
__package__ = "euler"
import itertools

from euler.base_n import int_base_n


def sumArithmeticSeries(a: float, d: float, n: int) -> float:
    """
    calculate sum of an arithmetic series
    :param a: first term of the series
    :param d: common difference
    :param n: number of terms
    :return: sum of the series
    """
    return (a + d * (n + 1) / 2) * n


def palindrome(length: int, base=10, ascending=False) -> [int_base_n]:
    """
    generator of palindrome numbers
    :param length: number of digits
    :param base: numeric base, default 10
    :param ascending: sort order, default descending
    :return: int palindrome number generator
    """
    assert isinstance(length, (int, int_base_n)) and \
           length > 0 and \
           isinstance(base, (int, int_base_n)) and \
           base > 0 and \
           isinstance(ascending, bool)

    if ascending:
        base_nums = tuple(x for x in range(0, base))
    else:
        base_nums = tuple(x for x in range(base - 1, -1, -1))

    num_choices = int((length - 1) / 2)

    for choices in itertools.product(base_nums[1:] if ascending else base_nums[:-1],
                                     *[base_nums for _ in range(num_choices)]):
        if length % 2 == 0:
            choices = choices + tuple(reversed(choices))
        else:
            choices = choices + tuple(reversed(choices[:-1]))
        yield int_base_n(sum([choices[i] * (base ** i) for i in range(0, len(choices))]), base=base)


if __name__ == "__main__":
    from time import time

    base = 10
    for input_number in [int(i) for i in input("enter numbers:").split()]:
        st = time()
        max_num = (base ** input_number) - 1
        min_num = base ** (input_number - 1)
        result = None
        for p in palindrome(2 * input_number, base=base):
            for x in range(max_num, min_num, -1):
                d, m = divmod(p, x)
                if m == 0 and d < max_num:
                    result = (p, int_base_n(x, base), d)
                    break
            if result: break
        et = time()
        print(result, "calculated in", et - st, "seconds")

    """ Problem #1
    x = int(sys.argv[1] if len(sys.argv) > 1 else input('number: '))
    st = time.time()
    result = int(sumArithmeticSeries(0, 3, int((x - 1) / 3)) + sumArithmeticSeries(0, 5, int((x - 1) / 5)) \
                 - sumArithmeticSeries(0, 15, int((x - 1) / 15)))
    et = time.time()
    print('Problem 001 solution for {0} is {1}; calculated in {2:n} seconds'.format(x, result, et - st))
    """
