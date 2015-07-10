#!/usr/bin/env python3
"""
Project Euler: https://projecteuler.net/problem=1
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
__author__ = 'Zuva Munshi'


def sum_series(a: float, d: float, n: int) -> float:
    """
    return the sum of an n terms of arithmetic series with first term a, common difference d
    :param a: first term
    :param d: common difference
    :param n: number of terms
    :return: sum of all terms of the series
    """
    return (a + d * (n - 1) / 2) * n


if __name__ == '__main__':
    from time import time

    for number in [int(x) for x in input("Enter numbers: ").split()]:
        st = time()
        max_term = number - 1
        result = sum_series(3, 3, int(max_term / 3)) \
                 + sum_series(5, 5, int(max_term / 5)) \
                 - sum_series(15, 15, int(max_term / 15))
        et = time()
        print("Sum of all multiples of 3 or 5 below {0} is {1}. Calculated in {2:0.6f} seconds".format(number, result,
                                                                                                       et - st))
