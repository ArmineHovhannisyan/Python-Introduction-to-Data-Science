# Task 1.3.1
# 1.Write a Python function, which gets 2 numbers, and return True if the second number is first number divider, otherwise False.
def isdivider(a, b):
    if b == 0:
        print('cant divide to 0')
        return False
    return a%b == 0
print(isdivider(4, 0)) #false
print(isdivider(4, 2)) #true
print(isdivider(5, 2)) #false


# 2.Write a Python function, which gets a number, and return True if that number is palindrome, otherwise False
def isPalindrome(n):
    temp = n
    reverse = 0
    while n > 0:
        currentDigit = n % 10
        reverse = reverse * 10 + currentDigit
        n = n // 10
    return temp == reverse

print(isPalindrome(10801)) #true
print(isPalindrome(1561))  #false

# 3.Write a Python function, which gets a number, and return True if that number is prime, otherwise False.
def isPrime(n):
    if n == 1:
        return  False
    else:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                return  False
                break
        else:
           return  True

print(isPrime(29)) #true
print(isPrime(8))  #false
print(isPrime(2))  #true
print(isPrime(1))  #false

# 4.Write a Python function, which checks if a number is perfect - that is equal to the sum of its proper positive divisors.
def isPerfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i
    return sum == n

print(isPerfect(6)) #true
print(isPerfect(8)) #false

# 5.Write a function, which gets 2 numbers, and return their Great common divisor
def getGreatCommonDivisor(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a