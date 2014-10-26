

def nameScore(name):
    return sum(map(lambda x: ord(x) - ord('A') + 1, name))


def nameScores():
    total = 0

    with open('p022_names.txt', 'r') as f:
        line = f.read().strip()
        names = sorted(line.split(','))
        names = [name.strip('"') for name in names]
        for index, name in enumerate(names):
            print index, name
            total += (index + 1) * nameScore(name)
    return total


print nameScores()
