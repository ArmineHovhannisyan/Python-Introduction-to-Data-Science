# Task 1.2.1
# 1.Write a Python program to get the largest number from a list.

list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Largest element is:", list1[-1])


# 2.Write a Python program to get the frequency of the given element in a list to.
list =  [1, 2, 1, 3, 5, 1, 5]
x = 1
print(list.count(x))


# 3.Write a Python program to remove the second element from a given list, if we know that the first elements index with that value is n.

x = int(input())
list = [1, 6, 2, 16, 6, 0] # remove second x ( x = 6 ). lets consider we have at least two 6 in our list
list.pop(list.index(x, list.index(x) + 1))

print(list)

