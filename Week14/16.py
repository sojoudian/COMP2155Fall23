import numpy

np16 = numpy.array([[1,2,3,4], [2,4,6,8], [3,6,9,12]])
print(np16)
print("*"*100)

print(np16.sum(axis=0))
print("*"*20)
print(np16.sum(axis=1))

print("*"*100)