import numpy
import pandas

# Data type in numpy
np2 = numpy.zeros(3)
t = np2.dtype
print(np2, t)

np2 = numpy.ones(3)
t = np2.dtype
print(np2, t)

np2 = numpy.array(['a', 1, 1.1])
t = np2.dtype
# UNICODE-32
print(np2, t)
