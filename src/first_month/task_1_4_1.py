# Task 1.4.1

# 1. Write a python program which returns a given list without duplicates.

def remove_duplicates(l):
    return list(set(l))


print(remove_duplicates([1, 2, 1, 35, 21, 9, 21, 'a']))

# 2. Write a python program which returns common elements of 2 lists.


def get_intersection(l1, l2):
    return set(l1) & set(l2)


l1 = [5, 10, 3, 9]
l2 = [1, 2, 5, 9, 36]
print(get_intersection(l1, l2))

# 3.Write a python program which return elements which are in first list but not in second


def get_difference(l1, l2):
    return set(l1) - set(l2)


l1 = [5, 10, 3, 9]
l2 = [1, 2, 5, 9, 36]

print(get_difference(l1, l2))


# 4.Write a python program which return elements are or in first list, either in second, but not in both
def get_sim_difference(l1, l2):
    return set(l1) ^ set(l2)


l1 = [5, 10, 3, 9]
l2 = [1, 2, 5, 9, 36]

print(get_sim_difference(l1, l2))


# 5.Write a python program which return elements which are or in first, either in second, or in both
def get_union(l1, l2):
    return set(l1) | set(l2)


l1 = [5, 10, 3, 9]
l2 = [1, 2, 5, 9, 36]

print(get_union(l1, l2))


# 6.Write  python function which get set and element value, and remove from set element with given value if exist

def remove_from_set(s, value):
    if value in s:
       s.remove(value)
    else:
       print(str(value) + ' is not in given set')
    return s

print(remove_from_set({1, 2, 3}, 2))
print(remove_from_set({1, 2, 3}, 4))

# 7.Write a python python program, which return list from given set, where each element of list, is equal to cub of set element

def get_cubes(s):
   cubes = []
   for i in s:
       cubes.append(i ** 3)
   return cubes

print(get_cubes({2, 3, 5, 2}))
