# Task 1.4.2

# 1.Write a python program, which adds a new value with the given key in dict.

def add_to_dict(key, value):
    d = {'a': 1, 'b': 2}
    d[key] = value
    return d

# or d.update({key: value})


print(add_to_dict('c', 3))


# 2.Write a python program which concat 2 dicts.

def concat(d1, d2):
    d = {**d1, **d2}

    return  d

d1 = {'a': 1, 'b': 2}
d2 = {'d': 1, 'b': 3}

print(concat(d1, d2))


# 3.Write a python program, which create a dictionary for given number N, where keys are numbers from 1 to N, and values are cubs of that numbers

def get_cubes(n):
    d_cubes = {}
    for i in range(1, n + 1):
        d_cubes[i] = i**3
    return d_cubes

print(get_cubes(7))


# 4.Write a python program which create dict from 2 lists with the same length
# we can apply set() to first list in case if there are duplicates. lets consider simple case


def create_dict(l_keys, l_values):

    length = len(l_keys)
    d = {}
    for i in range(0, length):
        d[l_keys[i]] = l_values[i]
    print(d)


l1 = [1, 2, 3, 4]
l2 = ['a', 'b', 'c', 'd']
create_dict(l1, l2)

# 5.Write a python program which gets the maximum and minimum values of a dictionary.


def get_maximum(d):
    max_value = list(d.values())[0]
    max_key = None
    for i in d:
        if d[i] > max_value:
            max_value = d[i]
            max_key = i
    print('maximum ' + max_key + ':' + str(max_value))


def get_minimum(d):
    min_value = list(d.values())[0]
    min_key = None
    for j in d:
        if d[j] < min_value:
            min_value = d[j]
            min_key = j
    print('minimum ' + min_key + ':' + str(min_value))


d = {'b': 2, 'c': 3, 'a': 1, 'd': 4}

get_minimum(d)
get_maximum(d)



# 6.Write a python program which combines 2 dictionaries into one, if there is an element with the same key, appropriate element of combined dict will be an element with that key, and sum of values as value.


def combine_with_sum(d1, d2):
    d3 = {**d1, **d2}
    for k, v in d3.items():
        if k in d1 and k in d2:
            d3[k] = v + d1[k]
    return d3


d1 = {'a': 1,'b': 2, 'c': 3,  'd': 4}
d2 = {'b': 6, 'e': 5 }
print(combine_with_sum(d1, d2))


# 7.Write a python program which create dict from string, where keys are letters of string, values are counts of letters in string


def char_frequency1(s):
    d = {}
    for i in s:
        if i in d.keys():
           d[i] += 1

        else:
            d[i] = 1
    return d


print(char_frequency1('armine hovhannisyan'))








