import numpy

np91 = numpy.loadtxt('data.csv', delimiter=',', skiprows=1, dtype=int)
print(np91)
print("*"*100)

# Indexing
print(np91[0])
print(np91[-1])
print(np91[0,3])
print(np91[1,3])