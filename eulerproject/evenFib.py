
MAX = 4000000

def fibonacci():
    fib = [0, 1]
    while True:
        next = fib[-1] + fib[-2]
        if next > MAX: return 
        fib.append(next)
        yield next

item = fibonacci()
print sum(filter(lambda x: x % 2 == 0, item))
