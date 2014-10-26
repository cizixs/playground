from operator import add


def sumSquareDifference(n):
    ''' return the difference between the square of the sum and the sum of
    the squares of the 1-n.'''
    nums = range(1, n+1)
    return pow(reduce(add, nums), 2) - reduce(add, map(lambda x: x*x, nums))

print sumSquareDifference(100)
