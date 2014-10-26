from operator import mul 


def smallestMultiple(n):
    ''' return the smallest number that can be divided by each of the numbers 
    from 1 to n without any remainder'''
    nums = [1]
    for i in range(2,n+1):
        j = i
        for num in nums:
            if j % num == 0:
                j = j / num
        if j != 1:
            nums.append(j)

    print nums
    return reduce(mul, nums)

print smallestMultiple(20)
