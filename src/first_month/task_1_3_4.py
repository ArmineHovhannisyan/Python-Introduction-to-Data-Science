#Task 1.3.4
# 1. Write a Python function, which Implements the Euler function.
# Euler function is return a count of numbers not great than N, which are mutually simple with N.
# Example  φ(6)=2, as only 1 and 5 from 1,2,3,4,5 are mutually simple with 6.

def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def Euler(n):
    count = 0
    for i in range(1, n):
        if (gcd(i, n) == 1):
            count += 1
    return count

print(Euler(0))   #0
print(Euler(1))   #0
print(Euler(8))   #4