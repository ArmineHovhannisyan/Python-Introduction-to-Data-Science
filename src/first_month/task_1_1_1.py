# Task 1.1.1

# 1.Given two whole numbers - the lengths of the legs of a right-angled triangle - output its area.

a = int(input())
b = int(input())
area = a * b / 2
print('The area of right angled triangle is equal: ', area)


# 2.Input a natural number n and output its last digit.

n = int(input())
lastDigit = n%10
print('last digit of n is:', lastDigit )


# 3.Input a two-digit natural number and output the sum of its digits.

n = int(input())
firstDigit = n//10
lastDigit = n%10
sum = firstDigit + lastDigit
print(sum)


# 4.You are given the first and second number in an arithmetic progression and natural number  n. Find n-th element of arithmetic progression.

a0 = int(input())
a1 = int(input())
n = int(input())
dif = a1 - a0;
nth = a0 + (n-1)*dif
print (nth)