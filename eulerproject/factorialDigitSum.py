from utils import factorial
from utils import sumDigit


def factorialDigitSum(n):
    fact = factorial(n)
    return sumDigit(fact)

print factorialDigitSum(100)
