import numpy

np91 = numpy.loadtxt('data.csv', delimiter=',', skiprows=1, dtype=int)
print(np91)
print("*"*100)

# SQL like Search!
found_indexes = numpy.where(np91 == 3)
print(found_indexes)