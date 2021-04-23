# Task 1.4.2

# 1.Write a python program, which adds a new value with the given key in dict.

d = {'a': 1, 'b': 2}
key = 'c'
value = 3
d[key] = value

# or d.update({key: value})
print(d)


# 2.Write a python program which concat 2 dicts.
d1 = {'a': 1, 'b': 2}
d2 = {'d': 1, 'b': 3}
d1.update(d2)
print(d1)


# 3.Write a python program, which create a dictionary for given number N, where keys are numbers from 1 to N, and values are cubs of that numbers
d_cubes = {}
n = 7
for i in range(1, n + 1):
    d_cubes[i] = i**3
print(d_cubes)


# 4.Write a python program which create dict from 2 lists with the same length
l_keys = [1, 2, 3, 4]
l_values = ['a', 'b', 'c', 'd']

#we can apply set() to first list in case if there are duplicates. lets consider simple case
length = len(l_keys)
d = {}
for i in range(0,length):
    d[l_keys[i]] = l_values[i]
print(d)


# 5.Write a python program which gets the maximum and minimum values of a dictionary.


# 6.Write a python program which combines 2 dictionaries into one, if there is an element with the same key, appropriate element of combined dict will be an element with that key, and sum of values as value.
# 7.Write a python program which create dict from string, where keys are letters of  string, values are counts of letters in string





