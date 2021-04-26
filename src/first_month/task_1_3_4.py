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



# 2.Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky
# if the sum of the first half of the digits is equal to the sum of the second half.
# Given a ticket number n, determine if it's lucky or not.

def isLucky(n):  #lets consider we're gonna input at least 2 digit number
    digits = []
    while n:
        digits.append(n % 10)
        n //= 10
    # return digits
    first_half_sum = 0
    second_half_sum = 0
    for i in range(len(digits) // 2):
        second_half_sum += digits[i]
    for i in range(len(digits) // 2, len(digits)):
        first_half_sum += digits[i]
    return first_half_sum == second_half_sum


print(isLucky(1230))
print(isLucky(1238))


# 3.The robot is standing on a rectangular grid and is currently located at the point (X0, Y0).
# The coordinates are integers. It receives N remote commands(list with n elements each of them is a command).
# Each command is one of : up, down, left, right. Upon receiving a correct command, the robot moves one unit in the given direction.
# If the robot receives an incorrect command, it simply ignores it. Where will the robot be located after following all the commands?
#Write a python function, which returns the sum of digits of given number N.

# 4. Write a python function, which returns the sum of digits of given number N.
def sumOfDigits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum
print(sumOfDigits(735))   #15



# 5.Write a python program to find the next smallest palindrome of a specified number. For example, for 119 next palindrome is 121.
def getNextPalindrome(n):
    digits = []
    while n:
        digits.append(n % 10)
        n //= 10

    digits = digits[::-1]
    lengt = len(digits)

    mid = int(lengt / 2)
    isLeftSmaller = False
    i = mid - 1

    j = mid + 1 if (lengt % 2) else mid

    while (i >= 0 and digits[i] == digits[j]):
        i -= 1
        j += 1

    if (i < 0 or digits[i] < digits[j]):
        isLeftSmaller = True

    while (i >= 0):
        digits[j] = digits[i]
        j += 1
        i -= 1

    if (isLeftSmaller):
        temp = 1
        i = mid - 1

        if (lengt % 2 == 1):
            digits[mid] += temp
            temp = int(digits[mid] // 10)
            digits[mid] %= 10
            j = mid + 1

        else:
            j = mid

        while (i >= 0):
            digits[i] += temp
            temp = int(digits[i] // 10)
            digits[i] %= 10
            digits[j] = digits[i]
            j += 1
            i -= 1

    palindrome = 0
    for k in range(0, lengt):
        palindrome += digits[k] * (10 ** k)
    return palindrome


print(getNextPalindrome(0))
print(getNextPalindrome(14454651321))
