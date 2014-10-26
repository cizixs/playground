
n = 500


def specialPythagoreanTrilplet():
    for a in range(3, n):
        for b in range(a+1, n):
            if a*a + b*b == pow(1000-a-b, 2):
                print a, b, 1000-a-b
                return a*b*(1000-a-b)


print specialPythagoreanTrilplet()
