vendor="Cisco"
print(vendor)
print(f'{vendor}'.encode())

bString=b'Cisco'
print(bString)

num = 123
print(f'{num}'.encode())

byteVar=b'Hello World!'
print(byteVar, "\n")
print(byteVar.decode())

# Data is sent through telnet as bytes
# Each byte created with 8 bit
# A bit is the smallest data size in computer
# bit can be 0 or 1
# Bit is 0, and 1 also means on or off