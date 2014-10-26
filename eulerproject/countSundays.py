from utils import daysOfMonth


def countSundays():
    ''' return the number of sundays fell on the first of the month.'''
    # 1 Jan 1990 was a Monday
    # from 1 Jan 1901 to 31 Dec 2000

    days = 365
    total = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if days % 7 == 6:
                total += 1
            days += daysOfMonth(month, year)

    return total

print countSundays()
