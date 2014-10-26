
MAX = 1000000

def isPalidrome(n):
    return str(n) == str(n)[::-1]


def isProduct(n, m):
    ''' n is product of two m digits numbers '''
    top,bottom = pow(10, m), pow(10, m-1)
    for i in xrange(top-1, bottom, -1):
        if n % i == 0 and bottom <= n / i < top:
            return True

    return False


def largestPalidromeProduct():
    n = MAX
    while True:
        if isPalidrome(n) and isProduct(n, 3):
            return n
        n -= 1

print largestPalidromeProduct()
