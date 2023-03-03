# Write a Python program to add the digits of a positive integer
# repeatedly until the result has a single digit.
# The input number will be greater than 0

# EX
# Input:
n1 = 48
# 4+8=12
# 1+2=3
# Output:
# 3

# Input
n2 = 59
# Output
# 5


def add_digits(n):
    while n > 9:
        n = sum(int(num) for num in str(n))
    return n


print(add_digits(n1))
print(add_digits(n2))


def add_digits(n):
    s = n
    while s > 9:
        s = str(s)
        o = 0
        for i in s:
            o += int(i)
        s = o
    return s


print(add_digits(n1))
print(add_digits(n2))
