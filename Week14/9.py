import numpy

np9 = numpy.loadtxt('data.csv', delimiter=',', skiprows=1)
print(np9)

np91 = numpy.loadtxt('data.csv', delimiter=',', skiprows=1, dtype=int)
print(np91)