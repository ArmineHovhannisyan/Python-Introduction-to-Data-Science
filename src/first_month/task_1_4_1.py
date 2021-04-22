# Task 1.4.1

# 1. Write a python program which returns a given list without duplicates.

l = [1 ,2, 1, 35, 21, 9, 21, 'a']
print(set(l))

# 2. Write a python program which returns common elements of 2 lists.

l1 = [5, 10 ,3, 9]
l2 = [1 ,2, 5, 9, 36]
l = set(l1) & set(l2)
print(l)

# 3.Write a python program which return elements which are in first list but not in second

l1 = [5, 10 ,3, 9]
l2 = [1 ,2, 5, 9, 36]
l = set(l1) - set(l2)
print(l)


# 4.Write a python program which return elements are or in first list, either in second, but not in both
l1 = [5, 10 ,3, 9]
l2 = [1 ,2, 5, 9, 36]
l = set(l1) ^ set(l2)
print(l)


# 5.Write a python program which return elements which are or in first, either in second, or in both
l1 = [5, 10 ,3, 9]
l2 = [1 ,2, 5, 9, 36]
l = set(l1) | set(l2)
print(l)


# 6.Write  python function which get set and element value, and remove from set element with given value if exist

def removeFromSet(s, value):
    if value in s:
       s.remove(value)
    else:
       print(str(value) + ' is not in given set')
    return s

print(removeFromSet({1, 2, 3}, 2))
print(removeFromSet({1, 2, 3}, 4))

# 7.Write a python python program, which return list from given set, where each element of list, is equal to cub of set element

def getCubes(s):
   cubes = []
   for i in s:
       cubes.append(i ** 2)
   return cubes

print(getCubes({2, 3, 5, 2}))
