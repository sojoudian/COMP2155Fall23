fileName=input("Enter name of the file: ")
CURRENT_FILE=open(fileName, "r")




print(CURRENT_FILE.read())
# print(CURRENT_FILE.read)
CURRENT_FILE.close()