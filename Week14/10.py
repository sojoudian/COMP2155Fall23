import numpy

np91 = numpy.loadtxt('data.csv', delimiter=',', skiprows=1, dtype=int)
print(np91)

# Get properties of the array
print(np91.ndim)
print(np91.shape)
print(np91.size)