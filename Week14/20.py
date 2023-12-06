import pandas
import numpy

# Dictionary data
data = {'first': 1, 'second':2, 'third': 3, 'fourth': 4, 'fifth': 5, 'sixth': 6, 'seventh': 7, 'eight': 8, 'ninth':9, 'tenth': 10}

p3 = pandas.Series(data)
print(p3['first'])
print('#'*40)

print(p3['first':'third'])
print('#'*40)

print(p3[['first','third']])
print('#'*40)

print(p3.get('first1', 'not found'))
print(p3.get('first', 'not found'))
print('#'*40)
print(p3.where(p3== 1))
print(p3.where(p3== 8))
