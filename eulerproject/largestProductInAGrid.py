from operator import mul


n = 20


def largestProductInAGrid():
    grid = []
    with open('problem11.txt', 'r') as f:
        for line in f:
            grid.append(map(int, line.strip().split()))

    max_product = 0
    for row in range(n):
        for col in range(n):
            # right
            if col < n - 3:
                product = reduce(mul, grid[row][col:col+4])
                max_product = max(product, max_product)
            # down
            if row < n - 3:
                product = reduce(mul, [grid[row+i][col] for i in range(4)])
                max_product = max(product, max_product)
            # diagonal
            if col < n - 3 and row < n - 3:
                product = reduce(mul, [grid[row+i][col+i] for i in range(4)])
                max_product = max(product, max_product)

    return max_product


print largestProductInAGrid()
