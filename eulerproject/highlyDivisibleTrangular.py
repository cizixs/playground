from utils import factors


def highlyDivisibleTrangularNumber(n):
    ''' return the first triangular number which has n divisors '''
    if n < 1:
        return 1

    start = 1
    while True:
        tri = start * (start + 1) / 2
        if len(factors(tri)) > n:
            return tri
        start += 1


print highlyDivisibleTrangularNumber(500)
