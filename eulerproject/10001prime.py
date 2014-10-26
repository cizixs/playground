from utils import isPrime


def nthPrime(n):
    num, count = 3, 1

    while True:
        if isPrime(num):
            count += 1
            if count == n:
                return num
        num += 2


print nthPrime(10001)
