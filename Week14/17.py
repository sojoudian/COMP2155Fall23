import pandas
import numpy

# DataFrames
data = list("hello")

df = pandas.Series(data)
print(df)

dfTwo = pandas.Series(data=data, index=(list(range(1,6))))
print(dfTwo)