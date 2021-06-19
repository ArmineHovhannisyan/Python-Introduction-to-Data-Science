import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# 1. Write a Pandas program to add, subtract, multiple and divide two Pandas Series

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 4, 'e': 5, 'f': 6}
s1 = pd.Series(data=d1, index=['a', 'b', 'c'])
s2 = pd.Series(data=d2, index=['d', 'e', 'f'])

s1.add(s2)

print(s1.add(s2))



# 2. Write a Pandas program to convert a dictionary to a Pandas series.

d = {'b': 1, 'x': 2,
     'l': 3, 'm': 5,
     'n': 8}

_series = pd.Series(d)

print(_series)

# 3. Write a Pandas program to convert a NumPy array to a Pandas series

np_array = np.array([0, -20, 3121, 404, 235])
print('np array: ' + str(np_array))
_series = pd.Series(np_array)

print(_series)

# 4. Write a Pandas program to convert the first column of a DataFrame as a Series
df = pd.DataFrame({"Letters": ["a", "b", "c"], "Numbers": [1, 2, 3]})
first_column = df.iloc[:, 0]
_series = pd.Series(first_column)

print('first column:' + str(_series))

# 5. Write a Pandas program to sort a given Series

#_series = pd.Series([19.5, 16.8, 22.78, 20.124, 18.1002])
_series = pd.Series(['Yerevan', 'Madrid', 'Berlin', 'Lisbon', '', 'Moscow'])

sorted_series = _series.sort_values()
print(sorted_series)

# 6. Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).
exam_data = {'name': ['Armine', 'Nare', 'Vlad', 'Nune', 'Elmira', 'Hayk', 'Anushavan'],
             'score': [15, 19, 16, 18, 19, 20, 14],
             'attempts': [1, 3, 2, 3, 2, 3, 1]}

df = pd.DataFrame(exam_data, index=exam_data['name'])
print(df[df['score'].between(15, 20)])


# 7. Write a Pandas program to calculate the sum of the examination attempts by the students.
print(df['attempts'].sum())


