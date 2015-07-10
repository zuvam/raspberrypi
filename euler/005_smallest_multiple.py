#!/usr/bin/env python3
"""
Project Euler: https://projecteuler.net/problem=5
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
__author__ = 'Zuva Munshi'


def lcm(x: int, y: int) -> int:
    """
    return least common multiple of two integers
    :param x: integer x
    :param y: integer y
    :return: lcm(x,y)
    """
    assert isinstance(x, int) and isinstance(y, int) and x > 0 and y > 0
    return int(x * y / gcd(x, y))


def gcd(x: int, y: int) -> int:
    """
    return the greatest common divisor of two integers
    :param x: integer x
    :param y: integer y
    :return: gcd(x,y)
    """
    assert isinstance(x, int) and isinstance(y, int) and x > 0 and y > 0
    while y != 0:
        x, y = y, x % y
    return x


def lcms(argg: range) -> int:
    """
    return least common multiple of a range of integers
    :param argg: generator of list of integers
    :return: lcm(argv[0], lcms(argv[1:])
    """
    l = 1
    for arg in argg:
        l = lcm(l, arg)
    return l


if __name__ == '__main__':
    from time import time

    for number in [int(n) for n in input("Enter numbers: ").split()]:
        st = time()
        try:
            result = lcms(range(1, number))
        except:
            result = '#could not compute#'
        et = time()
        print(
            "smallest number evenly divisible by integers from 1 to {0} is {1}. calculated in {2:0.6f} seconds".format(
                number, result, et - st))
