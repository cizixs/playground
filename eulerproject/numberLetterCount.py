

def letterCount(num):
    """ return the letter count in words for num """
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
             'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
             'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
             'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
            'eighty', 'ninety']

    total = 0

    words_dict = {key+1 : len(value) for key, value in enumerate(words)}
    tens_dict = {1 * (key + 2): len(value) for key, value in enumerate(tens)}

    small = num % 100
    if small == 0:
        pass
    elif small < 20:
        total += words_dict[small]
    elif small % 10 == 0:
        total += tens_dict[small / 10]
    else:
        total += tens_dict[small / 10]
        total +=  words_dict[small % 10]

    if num >= 100:
        total += words_dict[num / 100] + 10

    print num, total
    print words_dict
    print tens_dict
    return total


def numberLetterCount(n):
    ''' return number of all letters from 1 to n when written in words '''
    # n < 1000
    return sum(map(letterCount, range(1, n)))

print numberLetterCount(1000) + len('one thousand')
