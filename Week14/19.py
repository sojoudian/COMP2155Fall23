import pandas
import numpy

# Dictionary data
data = {'first': 1, 'second':2, 'third': 3, 'fourth': 4, 'fifth': 5, 'sixth': 6, 'seventh': 7, 'eight': 8, 'ninth':9, 'tenth': 10}

p2 = pandas.Series(data)


print(p2.head(1))
print('#'*70)
print(p2.tail(2))
print('#'*70)
print(p2.index)
print('#'*70)
print(p2.values)
print('#'*70)
