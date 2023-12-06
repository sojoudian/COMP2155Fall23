import numpy
import pandas

data = [1,2,3,numpy.nan,5,6]
unindexed = pandas.Series(data)

indeces = ['a', 'b', 'c', 'd', 'e', 'f']
indexed = pandas.Series(data, index=indeces)
print('indexed_1:\n', indexed)

data_dict = {'a': 1, 'b':2, 'c':3}
indexed = pandas.Series(data_dict)
print('\nindexed_2:\n', indexed)

fives = pandas.Series(5, indeces)
print('\nfives:\n', fives)

named = pandas.Series(data, name='mydata')
named.rename('\nmyData')
print(named.name)