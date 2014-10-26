from math import sqrt, ceil
from operator import mul


def isPrime(n):
    ''' return true if n is a prime'''
    top = int(ceil(sqrt(n))) + 1
    for i in range(2, top):
        if n % i == 0:
            return False

    return True


def isSquare(n):
    ''' return true is n = x*x '''
    if n < 0:
        raise ValueError("negative number has no root square")

    root = int(sqrt(n))
    return root * root == n


def factors(n):
    ''' return a list containing factors of n '''
    factors = [1]
    if n == 1:
        return factors
    if n <= 0:
        raise ValueError("can't calculate factors for non-positive number")

    root = int(sqrt(n))
    for i in range(2, root):
        if n % i == 0:
            factors.append(i)
            if i * i != n:
                factors.append(n / i)

    factors.append(n)
    return factors


def isLeapYear(year):
    ''' return true if a year is leap year'''
    return True if year % 400 == 0 or\
                   (year % 4 == 0 and year % 100 != 0) else False


def daysOfMonth(month, year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30

    return 29 if isLeapYear(year) else 28


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return reduce(mul, range(1, n+1))


def sumDigit(n):
    if n <= 0:
        return 0

    total = 0
    while n:
        total += n % 10
        n /= 10

    return total
