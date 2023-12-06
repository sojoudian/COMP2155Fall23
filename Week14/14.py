import numpy

# Save data to a file
numpy.savetxt('file.csv', numpy.arange(1,20,2), delimiter=',')
numpy.savetxt('hisory.csv', numpy.arange(1,20,2), delimiter=',', fmt='%.2f')

numpy.savetxt('record.csv', numpy.arange(1,20,2), delimiter=',', fmt='%i')