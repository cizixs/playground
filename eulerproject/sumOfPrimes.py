from utils import isPrime


MAX = 2000000


def sumOfPrimes(n):
    num = 3
    while num < n:
        if isPrime(num):
            yield num
        num += 2

print sum(sumOfPrimes(MAX)) + 2
