#!/usr/bin/env python3
# Solutions to Project Euler Problems
# About Project Euler: https://projecteuler.net
# List of Problems: https://projecteuler.net/archives
__author__ = 'Zuva Munshi'
__package__ = "euler"


class int_base_n(int):
    def __new__(cls, val: int, base: int):
        inst = super(int_base_n, cls).__new__(cls, val)
        inst.base = base
        return inst

    def digit_to_char(self, digit: int) -> str:
        if digit < 10: return str(digit)
        return chr(ord('a') + digit - 10)

    def str_base(self, number) -> str:
        if number < 0: return '-' + self.str_base(-number)
        (d, m) = divmod(int(number), self.base)
        if d > 0: return self.str_base(d) + self.digit_to_char(m)
        return self.digit_to_char(m)

    def __str__(self) -> str:
        return self.str_base(self)

    def __repr__(self) -> str:
        return self.str_base(self)

    def __divmod__(self, other):
        (d, m) = divmod(int(self), other)
        return int_base_n(d, self.base), int_base_n(m, self.base)
