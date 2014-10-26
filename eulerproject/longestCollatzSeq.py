
chains = {}


def collatzChain(n):
    if n == 1:
        return 1

    if n in chains:
        return chains[n]

    if n % 2 == 0:
        chain = collatzChain(n/2) + 1
    else:
        chain = collatzChain(3*n + 1) + 1

    chains[n] = chain
    return chain


max_chain = 0
num = 0
for i in range(2, 1000000):
    chain = collatzChain(i)
    if chain > max_chain:
        max_chain = chain
        num = i

print max_chain, num
