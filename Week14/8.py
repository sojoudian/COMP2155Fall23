import numpy

#from previous example:
np7 = numpy.random.randint(low=1, high=20, size=6)
print(np7)
np71 = numpy.random.randint(low=1, high=30, size=(2,3))
print(np71)

# Iterate through numpy arrray
for i in np7:
    print(i)

print("#"*100, "\n")    

for row in np71:
    print(row)
    for col in row:
        print(col)