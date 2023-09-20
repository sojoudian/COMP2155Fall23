myFile = open("wFile.txt", "r+")

firstTen = myFile.read(10)
print("Read string is:" + firstTen)

curr_p = myFile.tell()
print(curr_p)
sk = myFile.seek(2)


myFile.close()