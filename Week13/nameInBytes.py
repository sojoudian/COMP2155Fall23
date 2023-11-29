# Create a vraiable for your firstname
# Then iterate through all the characters in your firstname
# And output the byte value of each character

firstName="MaziAr"
for asciiValue in firstName.encode():
    print(asciiValue)

for index in range(len(firstName)):
    print(f'Character: {firstName[index]} bit value: {firstName.encode()[index]}')