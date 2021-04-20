# Task 1.1.2

# Strings

# 1.Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.

str = input()
strResult = str[:2] + str[-2:]
print(strResult)


# 2.Write a Python program to remove the nth index character from a nonempty string.

str = input()
n = int(input())
strResult = str[:n] + str[n+1:]
print(strResult)

# 3.Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

str = input()
length = len(str)
strResult = str[-1] + str[1:length -1] + str[0]
print(strResult)

# 4.Write a Python function to get a string made of 4 copies of the last two characters of a specified string

str = input()
length = len(str)
strResult =  4 * str[-2:]
print(strResult)


# List

# 1.Write a Python program that make a list from given string

str = 'armine'
print(list(str))



# 2.Write a Python program to print a new list which is the equivalent given list after removing the 0th, 4th and 5th elements.
list = [1, 2, 3, 4, 5, 6]
list.pop(0)
list.pop(3) #4-1 couse we deleted one item already. list was already changed
list.pop(3) #5-2 changed twice
print(list)


# 3.Write a Python program which add an element to the given list

list = [1, 2, 3, 4, 5]
x =  input() #different behavior depends on a type. we can consider simple case when x is a number
list.append(x)
print(list)


# 4.Write a Python program which concat 2 lists.
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list1.extend(list2)
print(list1)
