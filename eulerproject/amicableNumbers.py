from utils import factors


def sumOfProperDivisors(n):
    return sum(factors(n)) - n


def sumOfAmicableNumbers(n):
    total = 0

    for i in range(3, n):
        other = sumOfProperDivisors(i)
        if other < n and other > i and sumOfProperDivisors(other) == i:
            print other, i
            total += other + i

    return total

print sumOfAmicableNumbers(10000)
