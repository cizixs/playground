

def largeSum():
    total = 0
    with open('problem13.txt', 'r') as f:
        for line in f:
            num = int(line.strip())
            total += num

    return str(total)[:10]

print largeSum()
