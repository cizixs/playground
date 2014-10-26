

def powDigitSum(n):
    num = pow(2, n)
    total = 0
    while num:
        total += num % 10
        num /= 10
    return total

print powDigitSum(15)
print powDigitSum(1000)
