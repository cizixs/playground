from operator import mul


def largestProdctInSeries(n):
    max_product = 0

    with open('problem8.txt', 'r') as f:
        line = ''.join([line.strip() for line in f])
        for start in range(len(line) - n):
            product = reduce(mul, map(int, line[start:start+n]))
            if max_product < product:
                max_product = product

    return max_product

print largestProdctInSeries(13)
