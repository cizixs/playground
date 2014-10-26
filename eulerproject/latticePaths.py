

paths = {}


def latticePath(m, n):
    if m == 0 or n == 0:
        return 1
    else:
        if (m, n) in paths:
            return paths[(m,n)]
        path = latticePath(m-1, n) + latticePath(m, n-1)
        paths[(m,n)] = path
        return path


print latticePath(2, 2)
print latticePath(20, 20)
