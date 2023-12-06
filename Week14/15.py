import numpy

np1 = numpy.array(['a', 'b', 'c'])
np2 = numpy.array([1, 2, 3])

np15 = numpy.vstack((np1, np2))
print(np15)

np151 = numpy.hstack((np1, np2))
print(np151)