# -*- coding: utf-8 -*-
from math import ceil, sqrt


def largestFactor(n):
    if n < 3:
        return n
    if n <= 0:
        raise ValueError('can;t handle non-positive number')

    root = int(ceil(sqrt(n)))
    for x in range(2, root):
        if n % x == 0:
            return largestFactor(n/x)

    return n

print largestFactor(600851475143)
